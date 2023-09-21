"""Post-process DeformablePlate FEniCSx simulation outputs."""

import os

from typing import List, Optional

import pyvista as pv

from inductiva import structures, types, utils

SOLVER_OUTPUT_FILENAME = "results.xdmf"
TEMP_SOLVER_OUTPUT_FILENAME = "temp_results.xdmf"


class DeformablePlateOutput:
    """Post-process DeformablePlate FEniCSx simulation outputs."""

    def __init__(self, sim_output_path: types.Path):
        """Initializes a 'DeformablePlateOutput' object.

        Args:
            sim_output_path: Path to simulation output files.
        """
        self.sim_output_path = sim_output_path

    @utils.optional_deps.needs_structures_extra_deps
    def render(self,
               field_names: Optional[List[str]] = None,
               show_edges: bool = True,
               colormap: str = "jet",
               off_screen: bool = True,
               scalar_bar: bool = True,
               background_color: str = "white",
               transparent_background: bool = True) -> None:
        """Render the simulation fields as images.

        Args:
            field_names (list, optional): List of field names to render. Default
              is None.
            show_edges (bool, optional): Whether to display mesh edges. Default
              is True.
            colormap (str, optional): The colormap to apply to the field data.
              Default is "jet".
            off_screen (bool, optional): Whether to render the visualization 
              off-screen. Set to True for non-interactive rendering. Default is 
              True.
            scalar_bar (bool, optional): Whether to include a scalar bar legend
              in the visualization. Default is True.
            background_color (str, optional): The background color of the
              visualization. Default is "white".
            transparent_background (bool, optional): Whether the background of
              the saved images should be transparent. Default is True.
        """

        # Define the XDMF file path for the solver output file
        file_path = os.path.join(self.sim_output_path, SOLVER_OUTPUT_FILENAME)

        # Define a XDMF temporary file path
        temp_file_path = os.path.join(self.sim_output_path,
                                      TEMP_SOLVER_OUTPUT_FILENAME)

        # Remove time values from the XDMF file
        structures.utils.remove_time_values_from_xdmf(file_path, temp_file_path)

        # Read simulation output data
        reader = pv.get_reader(temp_file_path)
        py_multiblock = reader.read()

        # Get the list of available keys (field names) in the PyVista dataset
        keys = list(py_multiblock.keys())

        # Select the PyVista dataset representing the mesh
        pv_dataset = py_multiblock["mesh"]

        # Define a list of valid field names
        valid_field_names = [
            "displacement_x", "displacement_y", "displacement_z", "stress_xx",
            "stress_xy", "stress_xz", "stress_yx", "stress_yy", "stress_yz",
            "stress_zx", "stress_zy", "stress_zz", "strain_xx", "strain_xy",
            "strain_xz", "strain_yx", "strain_yy", "strain_yz", "strain_zx",
            "strain_zy", "strain_zz"
        ]

        # Iterate through the specified field names to render
        for field_name in field_names:

            if field_name != "von_mises" and field_name in valid_field_names:

                # Split the field_name into the main field and subfield
                # (e.g., stress_xx -> field='stress', subfield='xx')
                field, subfield = field_name.split("_")

                # Find the ID of the main field in the dataset keys
                field_id = keys.index(field)

                # Map the subfield string to an ID
                # (e.g., 'xx' -> 0, 'xy' -> 1, 'xz' -> 2)
                subfield_id = {
                    "x": 0,
                    "y": 1,
                    "z": 2,
                    "xx": 0,
                    "xy": 1,
                    "xz": 2,
                    "yx": 3,
                    "yy": 4,
                    "yz": 5,
                    "zx": 6,
                    "zy": 7,
                    "zz": 8
                }[subfield]

                # Extract the specific subfield array from the dataset
                field_array = py_multiblock[keys[field_id]].get_array(
                    0)[:, subfield_id]

            elif field_name == "von_mises" or field_name is None:
                # For the special case of "von_mises" field, find its index in
                # the dataset keys
                field_id = keys.index(field_name)

                # Extract the "von_mises" field array from the dataset
                field_array = py_multiblock[keys[field_id]].get_array(0)

            else:
                valid_field_names_str = ", ".join(valid_field_names)
                raise ValueError(
                    f"Invalid field_name {field_name}. "
                    f"Valid field names are: {valid_field_names_str}.")

            # Set the field_array in the point_data of the dataset
            pv_dataset.point_data[field_name] = field_array

        # Create the directory to save the field visualization images
        os.makedirs(os.path.join(self.sim_output_path, "fields"))

        # Define the path to save the field visualization as an image
        field_dir = os.path.join(self.sim_output_path, "fields")

        # Create a 2D fields visualizations from the PyVista dataset
        utils.visualization.create_2d_fields_from_pv_dataset(
            pv_dataset=pv_dataset,
            field_dir=field_dir,
            show_edges=show_edges,
            colormap=colormap,
            off_screen=off_screen,
            background_color=background_color,
            scalar_bar=scalar_bar,
            transparent_background=transparent_background)

        # Clean up temporary files and directory
        os.remove(temp_file_path)
