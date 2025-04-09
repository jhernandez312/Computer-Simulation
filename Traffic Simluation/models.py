import numpy as np
import random
import config
from functions import (
    init_road, add_cars, accelerate, decelerate, dally, move,
    distance, check_lanes, switch_lanes
)
from car import Car

# Create matrices using configuration values
matrix = np.full((config.iterations, config.num_cells), -1)
matrix2 = np.full((config.iterations, config.num_cells), -1)

def CA_model2(num_cars, p, left_vmax, right_vmax):
    cells = init_road(config.num_cells)
    cells2 = init_road(config.num_cells)
    random_cars = random.randint(0, num_cars)
    cells = add_cars(random_cars, cells, config.num_cells)
    cells2 = add_cars(num_cars - random_cars, cells2, config.num_cells)

    print("left lane:" + str(random_cars))
    print("right lane:" + str(num_cars - random_cars))

    for i in range(config.iterations):
        accelerate(cells, left_vmax, i, matrix)
        accelerate(cells2, right_vmax, i, matrix2)

        # check lanes start for left lane switching to right lane
        for j in range(len(cells)):
            if isinstance(cells[j], Car):
                if cells[j].curr_vel > 0 and cells[j].curr_vel > distance(cells, j, config.num_cells):
                    free = check_lanes(cells, cells2, j, cells, config.num_cells, config.left_vmax, config.right_vmax)
                    if free:
                        print("car " + str(j) + " switched to right lane")
                        switch_lanes(cells, cells2, j, cells, i, matrix, matrix2)

        # check lanes for right lane switching to left lane
        for j in range(len(cells2)):
            if isinstance(cells2[j], Car):
                if cells2[j].curr_vel > 0 and cells2[j].curr_vel > distance(cells2, j, config.num_cells):
                    free = check_lanes(cells, cells2, j, cells2, config.num_cells, config.left_vmax, config.right_vmax)
                    if free:
                        print("car " + str(j) + " switched to left lane")
                        switch_lanes(cells, cells2, j, cells2, i, matrix, matrix2)

        decelerate(cells, i, matrix)
        decelerate(cells2, i, matrix2)

        dally(cells, p, i, matrix)
        dally(cells2, p, i, matrix2)

        cells = move(cells, config.num_cells)
        cells2 = move(cells2, config.num_cells)

    return matrix, matrix2
