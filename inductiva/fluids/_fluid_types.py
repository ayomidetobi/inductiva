"""Physical properties of different fluid types."""

from inductiva_sph.sph_core.fluids import FluidProperties

WATER = FluidProperties(
    density=1e3,
    kinematic_viscosity=1e-6,
)

OIL = FluidProperties(
    density=878.7,
    kinematic_viscosity=0.32687,
)
