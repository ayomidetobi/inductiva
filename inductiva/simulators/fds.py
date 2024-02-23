"""FDS simulator module of the API."""

from typing import Optional

from inductiva import types, tasks, simulators
from inductiva.utils import meta


class FDS(simulators.Simulator):
    """Class to invoke a generic FDS simulation on the API."""

    def __init__(self):
        super().__init__()
        self.api_method_name = "fdm.fds.run_simulation"

    @meta.deprecated_arg(n_cores="n_vcpus")
    def run(self,
            input_dir: types.Path,
            sim_config_filename: str,
            n_vcpus: Optional[int] = None,
            use_hwthread: bool = True,
            post_processing_filename: str = None,
            on: Optional[types.ComputationalResources] = None,
            storage_dir: Optional[types.Path] = "",
            extra_metadata: Optional[dict] = None,
            **kwargs) -> tasks.Task:
        """Run the simulation.

        Args:
            input_dir: Path to the directory of the simulation input files.
            sim_config_filename: Name of the simulation configuration file.
            n_vcpus: Number of vCPUs to use in the simulation. If not provided
            (default), all vCPUs will be used.
            use_hwthread: If specified Open MPI will attempt to discover the
            number of hardware threads on the node, and use that as the
            number of slots available.
            on: The computational resource to launch the simulation on. If None
                the simulation is submitted to a machine in the default pool.
            other arguments: See the documentation of the base class.
        """
        return super().run(input_dir,
                           on=on,
                           input_filename=sim_config_filename,
                           post_processing_config=post_processing_filename,
                           storage_dir=storage_dir,
                           n_vcpus=n_vcpus,
                           use_hwthread=use_hwthread,
                           extra_metadata=extra_metadata)
