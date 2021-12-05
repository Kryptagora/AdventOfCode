import numpy as np

def get_points(p1, p2):
    """Returns points in the range - or flips it in case of p2 > p1"""

    return range(p1, p2+1) or range(p1, p2-1, -1)

def part_1(input_data: str, straight: bool=True):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    
    input_data = input_data.splitlines()

    # for shaping the array
    max_x, max_y = 0, 0

    mappings = []
    for line in input_data:
        x0, y0 = [int(i) for i in line.split("->")[0].strip().split(",")]
        x1, y1 = [int(i) for i in line.split("->")[1].strip().split(",")]

        if max(x0, x1) > max_x:
            max_x = max(x0, x1)
        elif max(y0, y1) > max_y:
            max_y = max(y0, y1)

        mappings.append([x0, y0, x1, y1])

    # make empty array
    world = np.zeros((max_x+1, max_y+1), dtype=np.int32)

    # fill array (note: to get the similar result rotate the matrix)
    for x0, y0, x1, y1 in mappings:
        if x0 == x1:
            world[x0, get_points(y0, y1)] += 1
        elif y0 == y1:
            world[get_points(x0, x1), y0] += 1

        # for part two
        elif not straight:
            for x, y in zip(get_points(x0, x1), get_points(y0, y1)):
                world[x, y] += 1

    return (world >= 2).sum().sum()


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""
    
    return part_1(input_data, straight=False)
