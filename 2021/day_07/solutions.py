import numpy as np

def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = np.array([int(i) for i in input_data.strip().split(",")])
    smallest_distance = np.inf

    for point in input_data:
        new_distance = sum(np.absolute(input_data - point))
        if new_distance < smallest_distance:
            smallest_distance = new_distance

    return (smallest_distance)


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = np.array([int(i) for i in input_data.strip().split(",")])

    upper = sum(triangle(abs(input_data - np.floor(np.mean(input_data)))))
    lower = sum(triangle(abs(input_data - np.ceil(np.mean(input_data)))))

    return int(min(upper, lower))

def triangle(x:int=0):
    return x * (x + 1) / 2
