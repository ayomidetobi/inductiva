"""Input parameters of SPH simulators."""
from enum import Enum
from typing import NamedTuple, Literal


class ParticleRadius(Enum):
    """Sets particle radius according to resolution."""
    HIGH = 0.008
    MEDIUM = 0.012
    LOW = 0.02


class SplishSPlasHParameters(NamedTuple):
    """Set of parameters for SPLisHSPlasH.

        Args:
            viscosity_solver: Method used to model the viscosity of the fluid.
             The available options are (the default is 'standard'):
                - 'None': Fluid is simulated with no viscosity.
                - 'Standard': Standard SPH formulation of viscosity. 
                - 'Weiler-2018': This method is based on the paper "A Physically
            cfl_method: cfl_method: Courant-Friedrichs-Lewy (CFL) method used for adaptive
              time stepping.
              The available options are (default is 'no'):
                - 'no': No adaptive time-stepping is used.
                - 'cfl': Use CFL condition.
                - 'cfl_p': Use CFL condition and consider number of pressure
                  solver iterations."""
    viscosity_solver = "Weiler-2018"
    cfl_method = "no"


class DualSPHysicsParameters(NamedTuple):
    """Set of parameters for DualSPHysics.

        Args:
            cfl_number: Coefficient to multiply dt.
            coefh: Coefficient to calculate the smoothing length in 3D.
            kernel: Interaction Kernel 1:Cubic Spline, 2:Wendland"""
    cflnumber = 0.2
    kernel = 1
