"Postprocessing steps for the MDWaterBox scenario."
import os
import MDAnalysis as mda
from MDAnalysis import transformations
import nglview as nv
from pathlib import Path
from typing import Literal


class ProteinSolvationOutput:
    """Post process the simulation output of a ProteinSolvation scenario."""

    def __init__(self, sim_output_path: Path = None):
        """Initializes a `ProteinSolvationOutput` object.

        Given a simulation output directory that contains the standard files
        generated by a ProteinSolvation simulation run, this class provides 
        methods to visualize the simulation outputs in a notebook interactively.

        Args:
            sim_output_path: Path to the simulation output directory."""

        self.sim_output_dir = sim_output_path

    def render_interactive(self,
                           representation: Literal["cartoon", "ball+stick",
                                                   "line", "point",
                                                   "ribbon"] = "ball+stick",
                           add_backbone: bool = True,
                           use_compressed_trajectory: bool = False):
        """Render the simulation outputs in an interactive visualization.
        Args: 
            representation: The protein representation to use for the 
            visualization.
            add_backbone: Whether to add the protein backbone to the 
            visualization.
            use_compressed_trajectory: Whether to use the compressed trajectory. 
            """
        topology = os.path.join(self.sim_output_dir, "solvated_protein.tpr")
        if use_compressed_trajectory:
            trajectory = os.path.join(self.sim_output_dir, "trajectory.xtc")
        else:
            trajectory = os.path.join(self.sim_output_dir,
                                      "solvated_protein.trr")

        universe = mda.Universe(topology, trajectory, all_coordinates=True)
        atoms = universe.atoms
        transformation = transformations.unwrap(atoms)
        universe.trajectory.add_transformations(transformation)
        view = nv.show_mdanalysis(universe)
        view.add_representation(representation, selection="not water")
        if add_backbone:
            view.add_representation("cartoon", selection="protein")
        view.center()
        view.background = "white"
        print("System Information:")
        print(f"Number of atoms in the system: {len(universe.atoms)}")
        print(f"Number of amino acids:"
              f"{universe.select_atoms('protein').n_residues}")
        print(f"Number of solvent molecules:"
              f"{universe.select_atoms('not protein').n_residues}")
        print(f"Number of trajectory frames: {len(universe.trajectory)}")
        return view
