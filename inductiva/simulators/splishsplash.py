"""SplisHSPlasH simulator module of the API."""
from typing import Optional

from inductiva import types, tasks, resources
from inductiva.simulators import Simulator


class SplishSplash(Simulator):
    """Class to invoke a generic SPlisHSPlasH simulation on the API."""

    def __init__(self):
        super().__init__()
        self.api_method_name = "sph.splishsplash.run_simulation"

    def run(
        self,
        input_dir: types.Path,
        sim_config_filename: str,
        on: Optional[resources.MachineGroup] = None,
        storage_dir: Optional[types.Path] = "",
        particle_radius: float = 0.025,
    ) -> tasks.Task:
        """Run the SPlisHSPlasH simulation.

        Args:
            input_dir: Path to the directory of the simulation input files.
            sim_config_filename: Name of the simulation configuration file.
            on: The computational resource to launch the simulation in. If None
                the simulation is launched in a machine of the default pool.
            storage_dir: Directory for storing simulation results.
            particle_radius: Radius of the particles in the simulation.
        Returns:
            Task object representing the simulation task.
        """
        return super().run(
            input_dir,
            on=on,
            input_filename=sim_config_filename,
            storage_dir=storage_dir,
            particle_radius=particle_radius,
        )
