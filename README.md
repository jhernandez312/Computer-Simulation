## Contagion

## Overview

This project simulates infectious disease dynamics using a well-mixed SIR model inspired by Chapter 21 of *Scientific Computing with Case Studies* by Dianne O’Leary. The objective is to explore epidemic behavior by solving ordinary differential equations (ODEs) for susceptible, infected, and recovered populations. A secondary part of the assignment extends the model by introducing vaccination policies.

## Tasks

1. **Well-Mixed SIR Model:**  
   - Implement the SIR model:
     - **Equations:**  
       \[
       \frac{dS}{dt} = -\tau S I, \quad \frac{dI}{dt} = \tau S I - \frac{I}{\kappa}, \quad \frac{dR}{dt} = \frac{I}{\kappa}
       \]
     - **Initial Conditions:**  
       \(S(0)=0.99\), \(I(0)=0.01\), \(R(0)=0\)
     - Use an ODE solver (e.g., Scipy’s `solve_ivp` or `odeint`) to simulate the epidemic until the infected fraction drops below \(10^{-4}\).

2. **Parameter Experiments:**  
   - Simulate the model for different parameter combinations:
     - \((\tau, \kappa) = (0.8, 4)\), \((0.4, 4)\), and \((0.8, 8)\).
   - Record the “stopping time” for each simulation and generate plots of \(S(t)\), \(I(t)\), and \(R(t)\).

3. **Parameter Sweep and Contour Plot:**  
   - Sweep across values of \(\tau \in (0, 4]\) and \(\kappa \in [1, 5]\).  
   - Create a contour plot or heatmap showing the time required for \(I(t)\) to drop below \(10^{-4}\).

4. **Vaccination Extension (For Teams Only):**  
   - Extend the model by adding a fourth compartment for vaccinated individuals \(V(t)\) with the conservation law:
     \[
     S + I + R + V = 1
     \]
   - Implement and compare two vaccination policies:
     - **Policy 1:** \(g_1(x) = \nu_1 S\)
     - **Policy 2:** \(g_2(x) = \nu_2 \frac{SI}{S+I}\)
   - Simulate and compare the performance of these vaccination strategies, examining trade-offs among the number vaccinated, infected, and overall epidemic duration.

## File Structure

The repository is organized into several Python modules for clarity and modularity:

- **`models.py`**:  
  Contains the ODE definitions for the contagion and vaccination models.

- **`simulation.py`**:  
  Includes functions for running simulations and computing stopping times.

- **`plotting.py`**:  
  Provides routines for line plots and contour plots summarizing simulation results.

- **`main.py`**:  
  Combines the simulation and plotting modules to run experiments and generate figures.

- **(Optional) `config.py`**:  
  Contains global parameters and configuration settings.

## How to Run

1. **Installation Requirements:**
   - Python 3.x
   - Required packages: `numpy`, `matplotlib`, `scipy`

2. **Run the Simulations:**
   - Open a terminal in the repository directory.
   - Execute the main script:
     ```bash
     python main.py
     ```
   - The script runs simulations for the specified parameter sets, displays time-evolution plots for \(S\), \(I\), and \(R\), and generates a contour plot from the parameter sweep.

## Results and Discussion

- **Simulation Output:**  
  The generated plots illustrate how the disease dynamics vary with different transmission rates (\(\tau\)) and recovery times (\(\kappa\)). Notably, the stopping times and peak infection levels change, providing insights into how quickly an epidemic might resolve.

- **Interpretation for Public Policy:**  
  The simulations indicate that faster disease transmission results in more rapid, but potentially shorter, epidemics. Adjustments in recovery times can significantly alter when the outbreak subsides. In the vaccination extension, you can see how different vaccination strategies trade off cost (number vaccinated) with disease control. These results are useful when advising public health strategies.

## References

- O’Leary, D. *Scientific Computing with Case Studies*. SIAM, 2009.

---
## Traffic Simulation

## Overview

This mini-project models one-dimensional traffic flow on a freeway using cellular automata (CA) models. The simulation is based on approaches described in Bungartz et al. (2014) and investigates the formation of traffic jams (stop-and-go traffic, shock waves) under various vehicle densities and with added stochastic behavior.

## Project Description

The project includes:

- **One-lane CA Model:**  
  Implements a basic cellular automata model (Algorithm 8.1 from the text) for simulating traffic flow on a single lane. The model factors in acceleration, deceleration, and a random dally effect.

- **Stochastic CA Model:**  
  Extends the one-lane model by adding stochastic behavior (Algorithm 8.2) via a "dally factor" parameter \(p\). Experiments include varying densities (10%, 25%, 50%, 80%) and different values for \(p\) (e.g., 0.1, 0.2, 0.5).

- **Two-lane Traffic Model:**  
  Further extends the simulation to two lanes with differing maximum speeds and incorporates cautious lane-changing rules to avoid collisions. Drivers show lane inertia by preferring to remain in their current lane until a deceleration is required.

## File Structure

- **`config.py`**  
  Contains global configuration settings (e.g., number of cars, maximum speeds, simulation iterations).

- **`car.py`**  
  Defines the `Car` class representing individual vehicles.

- **`functions.py`**  
  Implements utility functions for the simulation (e.g., road initialization, car placement, movement, distance calculations, and lane checking).

- **`models.py`**  
  Contains the implementations of the CA models for one-lane and two-lane traffic flow.

- **`main.py`**  
  Combines configuration, simulation execution, and plotting routines. Running this file starts the simulation and displays results via matplotlib plots.

## How to Run

1. **Prerequisites:**  
   Ensure Python is installed, along with the following packages:
   - `numpy`
   - `matplotlib`

2. **Run the Simulation:**  
   Open a terminal in the project directory and execute:
   ```bash
   python main.py
