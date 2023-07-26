"""Tools to analyze molecular dynamics simulations."""
import MDAnalysis as mda
from MDAnalysis import transformations


def unwrap_trajectory(topology, trajectory):
    """Unwrap the trajectory of a simulation to 
    remove effects from periodic boundary conditions.
    Args:
        topology: Path to the topology file.
        trajectory: Path to the trajectory file."""
    universe = mda.Universe(topology, trajectory, all_coordinates=True)
    atoms = universe.atoms
    transformation = transformations.unwrap(atoms)
    universe.trajectory.add_transformations(transformation)
    return universe
