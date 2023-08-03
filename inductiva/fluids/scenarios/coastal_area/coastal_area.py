"""Coastal area scenario."""

from functools import singledispatchmethod
import math
import os
from typing import Literal, Optional, Sequence
import shutil
from uuid import UUID

import numpy as np

from inductiva import tasks
from inductiva.scenarios import Scenario
from inductiva.simulation import Simulator
from inductiva.fluids.simulators import SWASH
from inductiva.utils.templates import (TEMPLATES_PATH,
                                       replace_params_in_template)
from inductiva.fluids.scenarios.coastal_area.output import CoastalAreaOutput

SCENARIO_TEMPLATE_DIR = os.path.join(TEMPLATES_PATH, "coastal_area")
SWASH_TEMPLATE_SUBDIR = "swash"
SWASH_CONFIG_TEMPLATE_FILENAME = "input.sws.jinja"
SWASH_CONFIG_FILENAME = "input.sws"
SWASH_BATHYMETRY_FILENAME = "bathymetry.bot"


class Bathymetry:
    """Represents a bathymetric profile.
    
    A bathymetric profile defines the depth of the sea bottom as a function of
    space, here described in Cartesian coordinates (x, y). Here, a bathymetry is
    represented as a 2D array with the depths, in meters, at each point of a
    regular grid. The grid is defined by the range of x and y values. Positive
    depths are below the water level.
    """

    def __init__(
        self,
        depths: np.ndarray,
        x_range: Sequence[float],
        y_range: Sequence[float],
    ):
        """Initializes a `Bathymetry` object.
        
        Args:
            depths: A 2D array with the depths, in meters. The first and second
              dimensions correspond to the x and y directions, respectively.
            x_range: The range of x values, in meters.
            y_range: The range of y values, in meters.
        """
        self.depths = depths
        self.x_range = x_range
        self.y_range = y_range

    @classmethod
    def from_text_file(
        cls,
        text_file_path: str,
        x_range: Sequence[float],
        y_range: Sequence[float],
    ):
        """Creates a `Bathymetry` object from a text file.
        
        The depth values are read from a text file. The text file must contain
        a 2D array with the depths, in meters. The first and second dimensions
        of the array in the text file (i.e. rows and columns) correspond to the
        x and y directions, respectively.

        Args:
            text_file_path: Path to the text file.
            x_range: The range of x values, in meters.
            y_range: The range of y values, in meters.
        """

        depths = np.loadtxt(text_file_path)
        return cls(depths, x_range, y_range)

    def to_text_file(self, text_file_path: str):
        """Writes the bathymetry to a text file.

        Args:
            text_file_path: Path to the text file.
        """

        np.savetxt(text_file_path, self.depths)

    @property
    def shape(self):
        """Returns the shape of the 2D array defining the bathymetry."""

        return self.depths.shape

    @property
    def x_delta(self):
        """Returns the distance between two consecutive points along x."""

        return (self.x_range[1] - self.x_range[0]) / self.shape[0]

    @property
    def y_delta(self):
        """Returns the distance between two consecutive points along y."""

        return (self.y_range[1] - self.y_range[0]) / self.shape[1]


class CoastalArea(Scenario):
    """Coastal area scenario.

    This is a simulation scenario for waves propagating in a coastal area
    represented by an arbitrary bathymetric profile (i.e., the map of depths of
    the sea bottom).

    The scenario is simulated in a 2D box (x points east, y points north) with
    dimensions defined by the bathymetric profile. Waves are injected from one
    of the boundaries of the simulation domain with a given amplitude and
    period. The base water level is also configurable.

    The remaining three boundaries of the simulation domain are absorbing.
    Absorption in these boundaries may not be perfect, so small reflections may
    be observed.

    Schematic representation of the simulation scenario: x points right, y
    points up.
    _________________________________
    |                               |
    |                               |
    |                               |
    |  injected waves ->     beach  |
    |                               |
    |                               |
    |_______________________________|
    Note that waves may be injected from other boundaries, and that the beach
    may be located elsewhere in the simulation domain.

    The scenario can be simulated with SWASH.
    """

    valid_simulators = [SWASH]

    def __init__(
        self,
        bathymetry: Bathymetry,
        water_level: float = 0,
        wave_source_location: Literal["N", "S", "E", "W"] = "W",
        wave_amplitude: float = 2,
        wave_period: float = 10,
    ):
        """Initializes a `CoastalArea` object.

        Args:
            bathymetry: The bathymetric profile.
            water_level: The water level, in meters.
            wave_source_location: The location of the wave source. Supported
              locations are: N (north), S (south), E (east), W (west),
              corresponding to the upper, lower, right and left boundaries of
              the simulation domain, respectively.
            wave_amplitude: The amplitude of the wave, in meters.
            wave_period: The period of the wave, in seconds.
        """
        self.bathymetry = bathymetry
        self.water_level = water_level
        self.wave_source_location = wave_source_location
        self.wave_amplitude = wave_amplitude
        self.wave_period = wave_period

    def simulate(
        self,
        simulator: Simulator = SWASH(),
        resource_pool_id: Optional[UUID] = None,
        run_async: bool = False,
        simulation_time: float = 100,
        time_step: float = 0.1,
        output_time_step: float = 1,
    ) -> tasks.Task:
        """Simulates the scenario.

        Args:
            simulator: Simulator to use. Supported simulators are: SWASH.
            resource_pool_id: Resource pool to use for the simulation.
            simulation_time: Total simulation time, in seconds.
            time_step: Time step, in seconds.
            output_time_step: Time step for the output, in seconds.
        """

        self.simulation_time = simulation_time
        self.time_step = time_step
        self.output_time_step = output_time_step

        task = super().simulate(
            simulator,
            resource_pool_id=resource_pool_id,
            run_async=run_async,
            sim_config_filename=SWASH_CONFIG_FILENAME,
        )

        task.set_output_class(CoastalAreaOutput)

        return task

    @singledispatchmethod
    def get_config_filename(self, simulator: Simulator):
        pass

    @singledispatchmethod
    def create_input_files(self, simulator: Simulator):
        pass


@CoastalArea.get_config_filename.register
def _(cls, simulator: SWASH):  # pylint: disable=unused-argument
    """Returns the configuration filename for SWASH."""
    return SWASH_CONFIG_FILENAME


@CoastalArea.create_input_files.register
def _(self, simulator: SWASH, input_dir):  # pylint: disable=unused-argument
    """Creates SPlisHSPlasH simulation input files."""

    template_files_dir = os.path.join(SCENARIO_TEMPLATE_DIR,
                                      SWASH_TEMPLATE_SUBDIR)

    shutil.copytree(template_files_dir,
                    input_dir,
                    dirs_exist_ok=True,
                    symlinks=True)

    config_template_file_path, config_file_path = (os.path.join(
        input_dir, file_name
    ) for file_name in [SWASH_CONFIG_TEMPLATE_FILENAME, SWASH_CONFIG_FILENAME])

    # SWASH requires the simulation time to be formatted as HHMMSS.sss.
    simulation_time_hmsms = _convert_time_to_hmsms(self.simulation_time)

    # SWASH uses as amplitude the peak-to-peak amplitude.
    wave_amplitude = 2 * self.wave_amplitude

    # All boundaries except the wave source are absorbing.
    absorbing_boundary_locations = ["N", "S", "E", "W"]
    absorbing_boundary_locations.remove(self.wave_source_location)

    replace_params_in_template(
        template_path=config_template_file_path,
        params={
            "bathymetry_filename": SWASH_BATHYMETRY_FILENAME,
            "x_range": self.bathymetry.x_range,
            "y_range": self.bathymetry.y_range,
            "x_num": self.bathymetry.shape[0] - 1,
            "y_num": self.bathymetry.shape[1] - 1,
            "x_delta": self.bathymetry.x_delta,
            "y_delta": self.bathymetry.y_delta,
            "water_level": self.water_level,
            "wave_source_location": self.wave_source_location,
            "wave_amplitude": wave_amplitude,
            "wave_period": self.wave_period,
            "absorbing_boundary_locations": absorbing_boundary_locations,
            "simulation_time_hmsms": simulation_time_hmsms,
            "time_step": self.time_step,
            "output_time_step": self.output_time_step,
        },
        output_file_path=config_file_path,
        remove_template=True,
    )

    bathymetry_file_path = os.path.join(input_dir, SWASH_BATHYMETRY_FILENAME)
    self.bathymetry.to_text_file(bathymetry_file_path)


def _convert_time_to_hmsms(time: float) -> str:
    """Converts time in seconds to hours, minutes, seconds and milliseconds.

    The output format is HHMMSS.sss, where HH, MM, SS and sss are the
    zero-padded values of hours, minutes, seconds and milliseconds in the time,
    respectively.
    """

    time_m, time_s = divmod(time, 60.)
    time_h, time_m = divmod(time_m, 60.)
    time_ms, time_s = math.modf(time_s)

    return (f"{int(time_h):02d}"
            f"{int(time_m):02d}"
            f"{int(time_s):02d}."
            f"{int(time_ms*1000):03d}")
