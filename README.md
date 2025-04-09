# Traffic Simulation

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
