"""Reef3D simulator module of the API."""

from typing import Optional

from inductiva import simulators, types, tasks


@simulators.simulator.mpi_enabled
class REEF3D(simulators.Simulator):
    """Class to invoke a generic FDS simulation on the API."""

    _API_METHOD_NAME = "reef3d"

    @property
    def api_method_name(self) -> str:
        return self._API_METHOD_NAME

    def run(
        self,
        input_dir: types.Path,
        on: Optional[types.ComputationalResources] = None,
        storage_dir: Optional[types.Path] = "",
        extra_metadata: Optional[dict] = None,
    ) -> tasks.Task:
        """Run the simulation.

        Args:
            input_dir: Path to the directory of the simulation input files.
            sim_config_filename: Name of the simulation configuration file.
            on: The computational resource to launch the simulation on. If None
                the simulation is submitted to a machine in the default pool.
            other arguments: See the documentation of the base class.
        """
        return super().run(input_dir,
                           on=on,
                           storage_dir=storage_dir,
                           extra_metadata=extra_metadata)
