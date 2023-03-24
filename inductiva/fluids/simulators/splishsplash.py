"""SplishSplash module of the API."""
import os
import pathlib
from typing import Literal

from absl import logging

import numpy as np
from tqdm import tqdm
import vtk
from vtk.util.numpy_support import vtk_to_numpy as _vtk_data_to_numpy
import xarray as xr

from inductiva.sph.splishsplash import run_simulation
from inductiva.types import Path


class SPlisHSPlasH:
    """Class to invoke a generic SPlisHSPlasH simulation on the API.

    Attributes:
        sim_dir: Path to the directory with all the simulation input files.
        input_filename: Name of the SPlisHSPlasH input file. The file should
            be present in `sim_dir`, and the name is relative to that
            directory. By default it is `splishsplash_input.json`.
    """

    def __init__(
        self,
        sim_dir: Path,
        input_filename: str = "splishsplash_input.json",
    ):
        self.input_filename = input_filename
        self.sim_dir = pathlib.Path(sim_dir)

        if not os.path.isdir(sim_dir):
            raise ValueError("The provided path is not a directory.")

    def simulate(self,
                 device: Literal["gpu", "cpu"] = "cpu",
                 output_dir=None) -> Path:
        """Run the simulation.

        Args:
            output_dir: Directory where the generated files will be stored.
        """
        return run_simulation(self.sim_dir,
                              self.input_filename,
                              device=device,
                              output_dir=output_dir)


def get_sorted_vtk_files(data_dir: str):
    """Returns a list of sorted vtk files in a directory."""

    if not os.path.exists(data_dir):
        raise IOError(f"Directory '{data_dir}' does not exist.")

    # Get a list of the files in the data directory.
    files = os.scandir(data_dir)

    # The files must have .vtk extension.
    files = [file for file in files if pathlib.Path(file.path).suffix == ".vtk"]

    # Sort the files to be read according to [file_key].
    def get_alphanum_key(file):
        file_name = pathlib.Path(file.path).stem
        file_name_splits = file_name.split("_")
        file_key = file_name_splits[-1]
        return int(file_key)

    files = sorted(files, key=get_alphanum_key)
    return files


def convert_vtk_data_dir_to_netcdf(
    data_dir: str,
    output_time_step: float,
    netcdf_data_dir: str,
):
    """Converts simulation output files to netcdf format.
   
    Args:
        data_dir: Data directory.
        output_time_step: Time step between output files, in seconds.
        netcdf_data_dir: Directory to store files in netcdf format.
    """

    files = get_sorted_vtk_files(data_dir)

    if not os.path.exists(netcdf_data_dir):
        os.makedirs(netcdf_data_dir)

    logging.info("Converting vtk files to netcdf format...")
    for file_key, file in tqdm(enumerate(files), total=len(files)):
        time = file_key * output_time_step
        xr_dataset = read_vtk_file_to_xr_dataset(file.path, time)
        file_stem = pathlib.Path(file.path).stem
        xr_dataset.to_netcdf(os.path.join(netcdf_data_dir, f"{file_stem}.nc"))


def read_vtk_file_to_xr_dataset(file_path: str, time: float) -> xr.Dataset:
    """Reads a single simulation output file to an xarray Dataset.
    
    Args:
        file_path: File path.
        time: Time instant, in seconds, associated with the data in the file.
    """

    if not os.path.exists(file_path):
        raise FileExistsError(f"File '{file_path}' not found.")

    if pathlib.Path(file_path).suffix != ".vtk":
        raise IOError(f"File '{file_path}' does not have .vtk extension.")

    time_var = xr.DataArray(np.asarray([time]),
                            attrs={
                                "units": "s",
                                "long_name": "$t$"
                            })

    data_vars = {}

    # Create vtk file reader.
    # SPlisHSPlasH saves particle data as an unstructured grid, so the
    # reader must be of that type.
    vtk_reader = vtk.vtkUnstructuredGridReader()

    # Set the file path in the reader.
    vtk_reader.SetFileName(file_path)
    vtk_reader.Update()

    # Read the file output, i.e. the type, size, etc. of its contents.
    vtk_output = vtk_reader.GetOutput()

    num_particles = vtk_output.GetNumberOfPoints()
    particle_idx_var = xr.DataArray(np.arange(num_particles),
                                    attrs={"long_name": "particle index"})

    # Read position data.
    position_data = _vtk_data_to_numpy(vtk_output.GetPoints().GetData())

    data_vars["x"] = xr.DataArray(
        position_data[np.newaxis, :, 0],
        dims=["time", "particle_idx"],
        coords=[time_var, particle_idx_var],
        attrs={
            "units": "m",
            "long_name": "$x$"
        },
    )

    data_vars["y"] = xr.DataArray(
        position_data[np.newaxis, :, 1],
        dims=["time", "particle_idx"],
        coords=[time_var, particle_idx_var],
        attrs={
            "units": "m",
            "long_name": "$y$"
        },
    )

    data_vars["z"] = xr.DataArray(
        position_data[np.newaxis, :, 2],
        dims=["time", "particle_idx"],
        coords=[time_var, particle_idx_var],
        attrs={
            "units": "m",
            "long_name": "$z$"
        },
    )

    # Read vtk point data, i.e. data associated with each particle other
    # than position.
    vtk_point_data = vtk_output.GetPointData()

    # Get names of all arrays of point data to validate data reading.
    vtk_point_data_array_names = [
        vtk_point_data.GetArray(idx).GetName()
        for idx in range(vtk_point_data.GetNumberOfArrays())
    ]

    if "velocity" in vtk_point_data_array_names:

        # Read velocity data.
        velocity_data = _vtk_data_to_numpy(vtk_point_data.GetArray("velocity"))

        data_vars["velocity_x"] = xr.DataArray(
            velocity_data[np.newaxis, :, 0],
            dims=["time", "particle_idx"],
            coords=[time_var, particle_idx_var],
            attrs={
                "units": "m/s",
                "long_name": "$v_x$"
            },
        )

        data_vars["velocity_y"] = xr.DataArray(
            velocity_data[np.newaxis, :, 1],
            dims=["time", "particle_idx"],
            coords=[time_var, particle_idx_var],
            attrs={
                "units": "m/s",
                "long_name": "$v_y$"
            },
        )

        data_vars["velocity_z"] = xr.DataArray(
            velocity_data[np.newaxis, :, 2],
            dims=["time", "particle_idx"],
            coords=[time_var, particle_idx_var],
            attrs={
                "units": "m/s",
                "long_name": "$v_z$"
            },
        )

    if "density" in vtk_point_data_array_names:

        # Read density data.
        density_data = _vtk_data_to_numpy(vtk_point_data.GetArray("density"))

        data_vars["density"] = xr.DataArray(
            density_data[np.newaxis, :],
            dims=["time", "particle_idx"],
            coords=[time_var, particle_idx_var],
            attrs={
                "units": "kg/m$^3$",
                "long_name": "$\\rho$"
            },
        )

    return xr.Dataset(data_vars)
