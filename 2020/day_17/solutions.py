import numpy as np
from scipy.ndimage import convolve

def part_1(input_data: str, dimension:int=3, steps:int=6):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    boolean_input_data = np.array([[atom == '#' for atom in line] for line in input_data], dtype=np.bool)
    kernel = np.ones(tuple(3 for i in range(dimension)), dtype=np.int32)

    if dimension == 3:
        kernel[1][1][1] = 0
    else:
        kernel[tuple(1 for i in range(dimension))] = 0

    gamefield = np.zeros((*(20 for i in range(dimension - 2)), 20, 20), dtype=np.int64)
    gamefield[tuple(steps for i in range(dimension - 2))] = np.pad(boolean_input_data, steps)

    for round in range(steps):
        convolution_result = convolve(gamefield, kernel, mode='constant')
        gamefield = np.where((convolution_result == 3) | (gamefield & (convolution_result == 2)), 1, 0)

    return gamefield.sum()


def part_2(input_data: str, dimension:int=4, steps:int=6):
    """Return second solution of puzzle."""

    return part_1(input_data=input_data, dimension=4, steps=6)
