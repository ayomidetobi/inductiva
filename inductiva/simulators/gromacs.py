"""GROMACS module of the API"""

from typing import Optional, List

from inductiva import types, tasks, simulators


class GROMACS(simulators.Simulator):
    """Class to invoke any GROMACS command on the API."""

    _API_METHOD_NAME = "gromacs"

    @property
    def api_method_name(self) -> str:
        return self._API_METHOD_NAME

    def run(
        self,
        input_dir: types.Path,
        commands: List[dict],
        on: Optional[types.ComputationalResources] = None,
        storage_dir: Optional[types.Path] = "",
        extra_metadata: Optional[dict] = None,
    ) -> tasks.Task:
        """Run a list of GROMACS commands.

        Args:
            input_dir: Path to the directory containing the input files.
            commands: List of commands to run using the GROMACS simulator.
            on: The computational resource to launch the simulation on. If None
                the simulation is submitted to a machine in the default pool.
            storage_dir: Parent directory for storing simulation
                               results.
        """

        return super().run(input_dir,
                           on=on,
                           commands=commands,
                           storage_dir=storage_dir,
                           extra_metadata=extra_metadata)
