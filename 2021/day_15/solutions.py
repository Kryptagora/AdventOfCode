import numpy as np
import heapq


def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    policy = np.array([list(i) for i in input_data], dtype=np.int32) - 1

    return find_path(policy)


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    policy = np.array([list(i) for i in input_data], dtype=np.int32) - 1

    policy = np.concatenate([policy+i for i in range(5)], axis=0)
    policy = np.concatenate([policy+i for i in range(5)], axis=1)

    return find_path(policy)


def find_path(policy:np.array=None):
    """Goes over all possible paths and returns smallest risk"""
    h, w = np.shape(policy)

    # starting point
    q = [(0,(0,0))]
    while q:
        risk, (x,y) = heapq.heappop(q)
        if (x,y) == (w-1,h-1):
            return risk

        for x,y in [(x,y+1),(x+1,y),(x,y-1),(x-1,y)]:
            if x >= 0 and x < w and y >= 0 and y < h and policy[y][x] >= 0:
                heapq.heappush(q, (risk+(policy[y][x] % 9)+1, (x,y)))

                # mark visited
                policy[y][x] = -1
