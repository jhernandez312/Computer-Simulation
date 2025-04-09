import random
import numpy as np
from car import Car
import config

def init_road(num_cells):
    return list(range(num_cells))

def add_cars(num_cars, cells, num_cells):
    count = 0
    while count != num_cars:
        spot = random.randint(0, num_cells - 1)
        if isinstance(cells[spot], int):
            cells[spot] = Car(random.randint(0, config.v_max), spot)
            count += 1
    return cells

def accelerate(cells, vmax, i, matrix):
    for j, cell in enumerate(cells):
        if isinstance(cell, Car):
            cell.curr_vel = min(cell.curr_vel + 1, vmax)  # accelerate
            matrix[i, j] = cell.curr_vel

def decelerate(cells, i, matrix):
    for j, cell in enumerate(cells):
        if isinstance(cell, Car):
            if cell.curr_vel > distance(cells, j, config.num_cells):
                cell.curr_vel = distance(cells, j, config.num_cells)  # decelerate
            matrix[i, j] = cell.curr_vel

def dally(cells, p, i, matrix):
    for j, cell in enumerate(cells):
        if isinstance(cell, Car):
            if random.random() < p:
                cell.curr_vel = max(cell.curr_vel - 1, 0)
            matrix[i, j] = cell.curr_vel

def move(cells, num_cells):
    new_cells = init_road(num_cells)
    for j, cell in enumerate(cells):
        if isinstance(cell, Car):
            cell.position = (j + cell.curr_vel) % num_cells
            new_cells[cell.position] = cell
    return new_cells

def distance(cells, index, num_cells):
    for dist in range(1, num_cells):
        next_index = (index + dist) % num_cells
        if isinstance(cells[next_index], Car):
            return dist - 1  # distance to next car
    return num_cells - 1

def switch_lanes(cells, cells2, index, curr_lane, i, matrix, matrix2):
    curr_car = curr_lane[index]
    if curr_lane == cells:  # switching from left lane to right lane
        curr_lane[index].curr_vel = min(curr_lane[index].curr_vel, config.right_vmax)
        cells[index] = -1
        matrix[i, index] = -1
        cells2[index] = curr_car
        matrix2[i, index] = curr_car.curr_vel
    elif curr_lane == cells2:  # switching from right lane to left lane
        curr_lane[index].curr_vel = min(curr_lane[index].curr_vel, config.left_vmax)
        cells2[index] = -1
        matrix2[i, index] = -1
        cells[index] = curr_car
        matrix[i, index] = curr_car.curr_vel


def check_lanes(cells, cells2, index, curr_lane, num_cells, left_vmax, right_vmax):
    """
    Check if it's safe for the car in curr_lane at position index to switch lanes.
    The check is done on the neighboring lane, verifying that both the forward and
    behind areas are free.

    Parameters:
      cells: list representing left lane cells.
      cells2: list representing right lane cells.
      index: current position (cell index) of the car.
      curr_lane: the lane (cells or cells2) the car is currently in.
      num_cells: total number of cells in the road.
      left_vmax: maximum velocity on the left lane.
      right_vmax: maximum velocity on the right lane.

    Returns:
      True if the adjacent lane is free both ahead and behind; otherwise, False.
    """
    curr_car = curr_lane[index]
    curr_vel = curr_car.curr_vel
    forward_free = True
    behind_free = True

    # --- check forward on the adjacent lane ---
    if curr_lane == cells:  # car is in left lane; check the right lane (cells2)
        for i in range(curr_vel):
            check_index = (index + i) % num_cells
            if isinstance(cells2[check_index], Car):
                forward_free = False
                break
    elif curr_lane == cells2:  # car is in right lane; check the left lane (cells)
        for i in range(curr_vel):
            check_index = (index + i) % num_cells
            if isinstance(cells[check_index], Car):
                forward_free = False
                break

    # --- check behind on the adjacent lane ---
    if curr_lane == cells:  # car is in left lane; check behind in the right lane (cells2)
        for i in range(right_vmax + 1):
            check_index = (index - i) % num_cells
            if isinstance(cells2[check_index], Car):
                # if a car behind is too close based on its velocity, the spot isn't free.
                if cells2[check_index].curr_vel >= i - 1:
                    behind_free = False
                    break
    elif curr_lane == cells2:  # car is in right lane; check behind in the left lane (cells)
        for i in range(left_vmax + 1):
            check_index = (index - i) % num_cells
            if isinstance(cells[check_index], Car):
                if cells[check_index].curr_vel >= i - 1:
                    behind_free = False
                    break

    return forward_free and behind_free

