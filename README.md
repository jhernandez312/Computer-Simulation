## Contagion

## Overview

This project simulates infectious disease dynamics using a well-mixed SIR model inspired by Chapter 21 of *Scientific Computing with Case Studies* by Dianne O’Leary. The objective is to explore epidemic behavior by solving ordinary differential equations (ODEs) for susceptible, infected, and recovered populations. A secondary part of the assignment extends the model by introducing vaccination policies.


## File Structure

The repository is organized into several Python files:

- **`models.py`**:  
  Contains the ODE definitions for the contagion and vaccination models.

- **`simulation.py`**:  
  Includes functions for running simulations and computing stopping times.

- **`plotting.py`**:  
  Provides routines for line plots and contour plots summarizing simulation results.

- **`main.py`**:  
  Combines the simulation and plotting modules to run experiments and generate figures.


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
## NYC Bike Share Simulation
# Mini-project 3: NYC Bike Share


This project implements a discrete-event simulation to study Citi Bike—New York City’s bike-sharing service. The goal is to build a simulation model that helps the NYC mayor and city planners determine how to best allocate a fixed number of bikes among the city’s stations to meet demand. The simulation is based on real-world data from Citi Bike usage and involves modeling rider arrivals, station selections, bike usage, and trip durations.

## Tasks

1. **Baseline Experiment:**  
   - With a fixed allocation of 10 bikes per station and 3,500 riders:
     - Estimate the **probability of a successful rental** (fraction of riders who pick up a bike).
     - Compute the **average waiting time** for riders who successfully get a bike.
     - Compute 90% confidence intervals for these estimates.
   - **Simulation Parameters:**
     - \(\lambda = 2.38\) riders per minute.
     - Ride times: \(\mu = 2.78\) and \(\sigma = 0.619\).
     - Start station probabilities from `start_station_probs.csv` and destination probabilities \(q_{i,j}\) derived from `trip_stats.csv`.

2. **Idealized Experiment:**  
   - Investigate a scenario with no limit on the number of bikes per station.
   - Determine, for each station, the minimum number of bikes needed to fully meet demand.


## File Structure



## How to Run

1. **Prerequisites:**  
   - Python 3.x  
   - Required libraries: `numpy`, `pandas`, `matplotlib`, `scipy`

2. **Setup:**  
   - Place the data files (`start_station_probs.csv`, `trip_stats.csv`, and, if applicable, `raw_trips.csv`) in the appropriate folder.
   - Install required libraries via pip if necessary:
     ```bash
     pip install numpy pandas matplotlib scipy
     ```

3. **Execute the Simulation:**  
   - From the project root directory, run:
     ```bash
     python main.py
     ```
   - This script will execute the simulation experiments and display the resulting plots and statistics.

## Verification & Findings

- **Verification:**  
  The simulation code was verified by comparing system performance metrics (e.g., successful rental probability and rider waiting time) against theoretical expectations and validating against the provided Citi Bike usage data.

- **Summary of Results:**  
  - The baseline experiment yields estimates for the probability of successful rentals and average waiting time (with 90% confidence intervals).
  - The idealized experiment illustrates the minimum required bikes per station to meet full demand.
  - For the pairs assignment, the analysis of raw trip data provides insights into arrival process assumptions and interarrival time distributions.

## References

- Citi Bike NYC: [https://citibikenyc.com/](https://citibikenyc.com/)


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
