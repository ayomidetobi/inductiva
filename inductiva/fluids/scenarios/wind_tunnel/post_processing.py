from functools import singledispatchmethod

import os
import pyvista as pv

from inductiva.simulation import Simulator
from inductiva.fluids.simulators import OpenFOAM
from inductiva.types import Path
from inductiva.utils.visualization import Object


class WindTunnelSimulationOutput:
    """Post process WindTunnel simulation outputs."""

    def __init__(self,
                 sim_output_path: Path,
                 time_step: int,
                 simulator: Simulator = OpenFOAM()):
        """Initializes an `OpenFOAMSimulationOutput` object.

        Args:
            simulator: Simulator object.
            sim_output_path: Path to simulation output files.
            time_step: Time step where we read the data.
        
        Attributes:
            sim_output_dir: path to the simulation directory
            object_path: path to the object insert in the WindTunnel
            post_processing_path: path to the post-processing data.
        """

        self.sim_output_dir = sim_output_path
        self.object_data = self.get_object_data(simulator, time_step)
        self.pressure_field = self.get_pressure_field(simulator, time_step)

    @singledispatchmethod
    def get_object_data(self, simulator: Simulator, time_step: int):
        return ValueError(
            f"Simulator not supported for `{self.__class__.__name__}` scenario."
        )

    @singledispatchmethod
    def get_pressure_field(self, simulator: Simulator, time_step: int):
        return ValueError(
            f"Simulator not supported for `{self.__class__.__name__}` scenario.")


@WindTunnelSimulationOutput.get_object_data.register
def _(self, simulator: OpenFOAM, time_step: int):
    """Get data over object for OpenFOAM."""

    reading_file = os.path.join(self.sim_output_dir, "foam.foam")
    open(reading_file, "w", encoding="utf-8").close()
    # Initialize reader and define reading time-step
    reader = pv.POpenFOAMReader(reading_file)
    reader.set_active_time_value(time_step)

    mesh = reader.read()
    object_data = mesh["boundary"]["object"]

    return object_data


@WindTunnelSimulationOutput.get_pressure_field.register
def _(self, simulator: OpenFOAM, time_step: int):
    """Returns pressure field over mesh points at a certain time_step."""

    pressure_field = Object(self.object_data, "p")

    return pressure_field
