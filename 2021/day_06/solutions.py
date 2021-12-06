import numpy as np

def part_1(input_data: str, days:int=80):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    
    input_data = np.array([int(i) for i in input_data.strip().split(",")], dtype=np.int32)

    for _ in range(days):
        input_data = update_fish(input_data)

    return len(input_data) 

    pass

def part_2(input_data: str, days:int=256):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    # counting array for all fishes
    fish = [*map(input_data.count, '012345678')]

    for _ in range(256):
        # cycle trough the fishes and add the value of new fishes
        fish = fish[1:] + [fish[0]]
        fish[6] += fish[-1]

    return sum(fish)


def update_fish(current: np.array=None):
    """Updates the list of Fishs given criterias"""

    # decrease every fish by 1
    current -= 1

    # count all fish that did reproduce and create new array
    count = np.count_nonzero(current == -1)
    add = np.full((count, ), 8)
    current = np.where(current == -1, 6, current)

    return np.concatenate((current, add), axis=None)