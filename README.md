
[![Python package](https://github.com/inductiva/inductiva/actions/workflows/python-package.yml/badge.svg)](https://github.com/inductiva/inductiva/actions/workflows/python-package.yml)

![linkedin_header](https://user-images.githubusercontent.com/104431973/231184851-0ce34289-593e-4832-aaa2-9aae652113f5.jpg)

## Large scale simulations made simple

Inductiva API provides dozens of open-source physical simulation packages from your laptop. Users can start simulating right away, with no hardware setup issues and no software configuration headaches. Additionally, we provide a transparent way to scale your simulations to the next-level with one-line of code.

One can **run** simulations in two ways:
- **High-level Simulation:** We provide pre-built scenarios that define a physical model (e.g., the dam break scenario in fluid dynamics). Users are allowed to define some parameters of the scenarios, choose the method of simulation with a few parameters and accelerate their simulations with the best hardware available for them. 

Example of how to run the dam break scenario:
```python
from inductiva import fluids

scenario = fluids.scenarios.DamBreak(dimensions=(1., 0.3, 0.3))

output = scenario.simulate()
video = output.render()
```

- **Low-level Simulation:** Users familiar with the simulators can submit their previously prepared simulation configuration files. In this way, users can immediatelly take advantage of performant hardware to speed up their simulations, without having to change any of their existing simulation scripts. Moreover, users may want to execute more than just one simulation and via API they can do it in a couple of lines of code. 

Example of how to run a low-level simulation:
```python
from inductiva import fluids

simulator = fluids.simulators.DualSPHysics()

output_dir = simulator.run(input_dir="FlowCylinder",
                           sim_config_filename="CaseFlowCylinder_Re200_Def.xml",
                           output_dir="Flow",
                           device="gpu")
```

Find more examples of simulations at the [tutorials section](https://github.com/inductiva/inductiva/tree/main/demos).

Our goal is to provide researchers and engineers with an easy and fast way to scale their simulations and explore various designs. 


## Simulators

The simulators we provide are all open-source and have their own dedicated documentation.

Currently, we have available the following simulators:
- [SPlisHSPlasH](https://github.com/InteractiveComputerGraphics/SPlisHSPlasH)
- [DualSPHysics](https://github.com/DualSPHysics/DualSPHysics)
- [OpenFOAM](https://www.openfoam.com/)
- [SWASH](https://swash.sourceforge.io/)
- [xBeach](https://oss.deltares.nl/web/xbeach/)
- [GROMACS](https://www.gromacs.org/)

If you would like other simulators to be added, contact us at [simulations@inductiva.ai](mailto:simulations@inductiva.ai).

## Scenarios

### Fluid block

This scenario simulates the motion of a fluid block in a unit cubic tank under
the action of gravity. The fluid motion is simulated using the [Smoothed
Particle Hydrodynamics](https://en.wikipedia.org/wiki/Smoothed-particle_hydrodynamics)
method. The fluid block is initialized with a given velocity, dimensions and
physical properties (density and viscosity).

#### Example

Initialize the scenario:

```python
from inductiva import fluids
scenario = fluids.scenarios.FluidBlock(density=1e3,
                                       kinematic_viscosity=1e-6,
                                       position=(0.3, 0.3, 0.3),
                                       dimensions=(0.4, 0.4, 0.4),
                                       initial_velocity=(0.0, 0.0, 0.0))
```

The user can specify the fluid density (in kg/m^3), kinematic viscosity (in
m^2/s), initial position (in m), dimensions (in m) and velocity (in m/s).

Run the simulation:

```python
output = scenario.simulate(simulator=fluids.SPlisHSPlasH(),
                           simulation_time=1,
                           time_step=0.001,
                           output_time_step=0.05)
```

The user can specify the total simulation time, the adopted time step and the
time step between outputs (all in seconds). By default, the simulation is run
with SPliSHSPlasH, but the user can specify a different simulator. The available
simulators for this scenario are SPlisHSPlasH and DualSPHysics.

Visualize the results:

```python
output.render()
```

\[TODO @IvanPombo: add gif with render\]

### Fluid tank

This scenario simulates the motion of a fluid in a cubic or cylindrical tank.
Fluid is injected in the tank via an inlet located at the top of the tank, and
flows out of the tank via an outlet located at the bottom of the tank. The
motion of the fluid is controled by gravity. The simulation is performed using
the [Smoothed Particle Hydrodynamics](https://en.wikipedia.org/wiki/Smoothed-particle_hydrodynamics)
method.

#### Example

Initialize the scenario:

```python
from inductiva import fluids
scenario = fluids.scenarios.FluidTank(fluid=fluids.WATER, fluid_level=0.5)
```

The user can specify the fluid (e.g. water, honey or oil), the fluid level (in
meters), as well as the tank shape and its inlet and outlet properties.

Run the simulation:

```python
output = scenario.simulate(simulation_time=5,
                           output_time_step=0.1,
                           resolution="medium")
```

The user can specify the total simulation time and the time step between outputs
(all in seconds). The user can also specify the resolution of the simulation
(low, medium or high).

Visualize the results:

```python
output.render()
```

![Fluid tank simulation.](resources/media/fluid_tank.gif)

### Coastal area

This scenario simulates the propagation of waves in a coastal area, by solving
the [shallow water equations](https://en.wikipedia.org/wiki/Shallow_water_equations)
in a given bathymetric profile (i.e., the depth of the sea bottom). For now,
this profile is fixed to be that of Praia do Carneiro beach, in Porto, Portugal.
Waves are injected at the boundary opposite to the beach, and propagate towards
the shore, interacting with the different elements of the bathymetry.

#### Example

Initialize the scenario:

```python
from inductiva.fluids.scenarios import CoastalArea

scenario = CoastalArea(wave_amplitude=2.5, wave_period=5.5, water_level=1.0)
```

The user can specify the wave amplitude (in meters) and period (in seconds), as
well as the base water level (in meters).

Run the simulation:

```python
output = scenario.simulate(simulation_time=120, time_step=0.1, output_time_step=1)
```

The user can specify the total simulation time, the adopted time step and the
time step between outputs (all in seconds).

Visualize the results:

```python
output.render(quantity="water_level")
```

This produces a movie of the temporal evolution of the water level in the
coastal area.

![Coastal area simulation. Water level render.](resources/media/coastal_area.gif)


### MDWaterBox

This scenario simulates a system that consists of a cubic box of water molecules, evolving according to the rules of Molecular Dynamics - the position of the water molecules is updated using Newton's equation in discrete time steps. The force that acts upon the particles is computed using standard molecular force fields. This approach is inspired by [this article](https://arxiv.org/abs/2112.03383).

#### Example

First we initialize the scenario:
```
from inductiva.molecules.scenarios import MDWaterBox

scenario = MDWaterBox(temperature = 300, box_size = 2.3)
```

The user can specify the temperature (in Kelvin) and box size (length of one of the cube's edges, in nanometers). The numbers above correspond to the default values.

After the initialization, we are ready to simulate the system:

```
output = scenario.simulate(simulation_time = 10,
            nsteps_minim = 5000)
```

The simulate method initializes a simulation in the cloud. In this call, we set the parameters:
 - simulation_time = 10: sets the trajectories time to span 10 **nanosecons**;
 -nsteps_minin = 5000: sets the number of minimization steps in the energy minimization step. 

When the simulation ends, the simulation output files can be found in inductiva_output/task_id folder. Also, the object simulation can be used to visualize some aspects of the outputs. In particular, ```output.render_interactive()``` yields an interactive visualization that can be visualized in a standard jupyter notebook.

### ProteinSolvation

This scenario simulates the dynamics of a protein whose structure is described by a PDB file. The protein is placed in a cubic box filled with water. If the protein has a non-zero electric charge, charged ions are added to the solution to neutralize the system. First, the system undergoes an [energy minimization step](), in which it is ensured that the structure of the protein+water system doesn't have steric clashes and structural issues. Then, the position of the atoms in this system is updated using Newton's equation in discrete time steps. The force that acts upon the particles is computed using standard molecular force fields.

#### Example

First we initialize the scenario:
```
from inductiva.molecules.scenarios import ProteinSolvation

scenario = ProteinSolvation(pdb_file, temperature = 300)
```

The user must provide the path for the PDB file  ```pdb_file``` corresponding to the protein the user wants to simulate. Also, it can specify the temperature (in Kelvin). The number above correspond to the default value.

After the initialization, we are ready to simulate the system:

```
output = scenario.simulate(simulation_time = 10,
            nsteps_minim = 5000)
```

The simulate method initializes the simulation. In this call, we set the parameters:
 - simulation_time = 10: sets the trajectories time to span 10 **nanosecons**;
 -nsteps_minin = 5000: number of steps for the energy minimization section. 

When the simulation ends, the simulation output files can be found in inductiva_output/task_id folder. Also, the object simulation can be used to visualize some aspects of the outputs. In particular, ```output.render_interactive()``` yields an interactive visualization that can be visualized in a standard jupyter notebook.

## Installation

It is super simple to start using the API if you are already familiar with Python package management.
One just needs to do
```
pip install inductiva
```

and your are good to go! You are ready to start [exploring our tutorial notebooks](https://github.com/inductiva/inductiva/tree/main/demos).

Notice that, in a local computer you just need to do this once. When opening the tutorials in Google Colab, you may need to re-install this
between notebooks.

## API access tokens

Please request your demo API token via the following Google Form (we will reply to you by email):

[Request API token](https://docs.google.com/forms/d/e/1FAIpQLSflytIIwzaBE_ZzoRloVm3uTo1OQCH6Cqhw3bhFVnC61s7Wmw/viewform)

