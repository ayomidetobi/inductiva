"""Protein solvation scenario."""

from functools import singledispatchmethod
from typing import Optional, Literal
import os
import shutil

from inductiva import tasks, resources, simulators, scenarios, utils, molecules

SCENARIO_TEMPLATE_DIR = os.path.join(utils.templates.TEMPLATES_PATH,
                                     "protein_solvation")
GROMACS_TEMPLATE_INPUT_DIR = "gromacs"
COMMANDS_TEMPLATE_FILE_NAME = "commands.json"


class ProteinSolvation(scenarios.Scenario):
    """Solvated protein scenario."""

    valid_simulators = [simulators.Gromacs]

    def __init__(self, protein_pdb: str, temperature: float = 300):
        """
        Scenario constructor for protein solvation based on the GROMACS
        simulator.
        The three main steps of this scenario are solvation, energy minimization
        and simulation. The user can control the number of steps used to perform
        the energy minimization step and the duration, temperature and
        integrator used to perform the simulation.
        Args:
            protein_pdb: The path to the protein pdb file.
            temperature: The temperature to use for the simulation.
            charged: Whether the protein is charged or not. If None, the charge
            is computed automatically.
        """
        self.template_dir = os.path.join(SCENARIO_TEMPLATE_DIR,
                                         GROMACS_TEMPLATE_INPUT_DIR)
        self.protein_pdb = utils.files.resolve_path(protein_pdb)
        self.temperature = temperature

    def set_default_output_files(self):
        """Set the default output files for the Protein Solvation Scenario.

        Instead of downloading the full trajectory, the user can choose
        to download only the compressed trajectory file. The following files
        are set as the default ones, and will be the only ones downloaded if
        the user does not require the full trajectory at task.get_output()."""

        return [
            "protein.gro", "compressed_trajectory.xtc", "solvated_protein.tpr",
            "topol.top", "rmsf_values.npy"
        ]

    def simulate(
            self,
            simulator: simulators.Simulator = simulators.Gromacs(),
            machine_group: Optional[resources.MachineGroup] = None,
            run_async: bool = False,
            simulation_time_ns: float = 10,  # ns
            output_timestep_ps: float = 1,  # ps
            integrator: Literal["md", "sd", "bd"] = "md",
            n_steps_min: int = 5000) -> tasks.Task:
        """Simulate the solvation of a protein.

        Args:
            machine_group: The machine group to use for the simulation.
            simulation_time_ns: The simulation time in ns.
            output_timestep_ps: The output timestep in ps.
            integrator: The integrator to use for the simulation. Options:
                - "md" (Molecular Dynamics): Accurate leap-frog algorithm for
                integrating Newton's equations of motion.
                - "sd" (Steepest Descent): Stochastic dynamics integrator with
                leap-frog scheme.
                - "bd" (Brownian Dynamics): Euler integrator for Brownian or
                position Langevin dynamics.

            For more details on the integrators, refer to the GROMACS
            documentation at
            https://manual.gromacs.org/current/user-guide/mdp-options.html.

            n_steps_min: Number of steps for energy minimization.
            run_async: Whether to run the simulation asynchronously.
        """
        simulator.override_api_method_prefix("proteinsolvation")

        self.nsteps = int(
            simulation_time_ns * 1e6 / 2
        )  # convert to fs and divide by the time step of the simulation (2 fs)
        self.output_frequency = int(
            output_timestep_ps * 1000 /
            2)  # convert to fs and divide by the time step
        # of the simulation (2 fs)
        self.integrator = integrator
        self.n_steps_min = n_steps_min
        commands = self.get_commands()

        task = super().simulate(simulator,
                                machine_group=machine_group,
                                commands=commands,
                                run_async=run_async)

        task.set_output_class(molecules.ProteinSolvationOutput)
        task.set_default_output_files(self.set_default_output_files())

        return task

    def get_commands(self):
        """Returns the commands for the simulation."""

        commands_template_path = os.path.join(SCENARIO_TEMPLATE_DIR,
                                              GROMACS_TEMPLATE_INPUT_DIR,
                                              COMMANDS_TEMPLATE_FILE_NAME)

        commands = self.read_commands_from_file(commands_template_path)
        return commands

    @singledispatchmethod
    def create_input_files(self, simulator: simulators.Simulator):
        pass


@ProteinSolvation.create_input_files.register
def _(self, simulator: simulators.Gromacs, input_dir):  # pylint: disable=unused-argument
    """Creates GROMACS simulation input files."""

    # rename the pdb file to comply with the naming in the commands list
    shutil.copy(self.protein_pdb, os.path.join(input_dir, "protein.pdb"))

    template_files_dir = os.path.join(SCENARIO_TEMPLATE_DIR,
                                      GROMACS_TEMPLATE_INPUT_DIR)

    shutil.copytree(template_files_dir, input_dir, dirs_exist_ok=True)

    utils.templates.batch_replace_params_in_template(
        templates_dir=input_dir,
        template_filenames=[
            "simulation.mdp.jinja",
            "energy_minimization.mdp.jinja",
        ],
        params={
            "integrator": self.integrator,
            "nsteps": self.nsteps,
            "ref_temp": self.temperature,
            "nsteps_minim": self.n_steps_min,
            "output_frequency": self.output_frequency,
        },
        output_filename_paths=[
            os.path.join(input_dir, "simulation.mdp"),
            os.path.join(input_dir, "energy_minimization.mdp"),
        ],
        remove_templates=True,
    )
