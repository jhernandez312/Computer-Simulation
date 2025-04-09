import random
import numpy as np
import matplotlib.pyplot as plt
import config
import models

from car import Car
from functions import (
    init_road, add_cars, accelerate, decelerate, dally, move,
    distance, check_lanes, switch_lanes
)
from models import CA_model2

###########################################
#           PLOTTING FUNCTIONS
###########################################
def plot_matrix(matrix, title):
    plt.matshow(matrix, cmap='tab10')
    plt.colorbar()
    plt.title(title, pad=20)
    plt.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    plt.ylabel('Iteration')
    plt.show()

###########################################
#                MAIN FUNCTION
###########################################
def main():
    # Run the cellular automata model for two lanes simulation.
    # CA_model2 is assumed to use the provided global parameters appropriately.
    matrix_left, matrix_right = CA_model2(config.num_cars, config.p, config.left_vmax, config.right_vmax)

    # Plot the resulting matrices for each lane.
    plot_matrix(matrix_left, 'Left Lane')
    plot_matrix(matrix_right, 'Right Lane')

if __name__ == '__main__':
    main()
