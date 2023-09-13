"""Describes the physical scenarios and runs its simulation via API."""
from typing import List, Literal, Optional
from enum import Enum
from dataclasses import dataclass

from inductiva import tasks, resources
from inductiva.simulators import Simulator
from inductiva.simulators import DualSPHysics
from inductiva.fluids.fluid_block import FluidBlock
from inductiva.fluids.fluid_types import FluidType
from inductiva.fluids.fluid_types import WATER

from inductiva.fluids._post_processing import SPHSimulationOutput


@dataclass
class ParticleRadius(Enum):
    """Sets particle radius according to resolution."""
    HIGH = 0.008
    MEDIUM = 0.012
    LOW = 0.02


class DamBreak(FluidBlock):
    """Physical scenario of a dam break simulation."""

    def __init__(
        self,
        fluid: FluidType = WATER,
        dimensions: Optional[List[float]] = None,
        position: Optional[List[float]] = None,
    ):
        """Initializes a `DamBreak` object.

        Args:
            fluid: A fluid type to simulate.
            dimensions: A list containing fluid column dimensions,
              in meters.
            pisition: A list containing fluid column position in a tank,
              in meters.
            """

        if dimensions is None:
            dimensions = [0.3, 1, 1]

        super().__init__(density=fluid.density,
                         kinematic_viscosity=fluid.kinematic_viscosity,
                         dimensions=dimensions,
                         position=position)

    # pylint: disable=arguments-renamed
    def simulate(
        self,
        simulator: Simulator = DualSPHysics(),
        machine_group: Optional[resources.MachineGroup] = None,
        device: Literal["cpu", "gpu"] = "cpu",
        resolution: Literal["high", "medium", "low"] = "medium",
        simulation_time: float = 1,
        run_async: bool = False,
    ) -> tasks.Task:
        """Simulates the scenario.

        Args:
            simulator: Simulator to use.
            machine_group: The machine group to use for the simulation.
            device: Device in which to run the simulation.
            resolution: Resolution of the simulation.
            simulation_time: Simulation time, in seconds.
            run_async: Whether to run the simulation asynchronously.
        """

        particle_radius = ParticleRadius[resolution.upper()].value

        task = super().simulate(simulator=simulator,
                                machine_group=machine_group,
                                device=device,
                                particle_radius=particle_radius,
                                simulation_time=simulation_time,
                                run_async=run_async)

        task.set_output_class(SPHSimulationOutput)

        return task
