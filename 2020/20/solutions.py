from tqdm import tqdm
import numpy as np
import operator
import networkx
import itertools
import functools
import re

class Tile:
    def __init__(self, id_number, content):
        self.id_number = id_number
        self.content = content
        self.count_rotations = 0


    def rotate(self):
        self.content = np.rot90(self.content)
        self.count_rotations += 1
        return self

    def _reset_rotations_(self):
        self.count_rotations = 0

    def flip(self):
        self.content = np.flip(self.content)
        return self

    def get_flips(self):
        res = self.content
        for f in [True, False]:
            for i in range(4):
                yield res
                res = np.rot90(res)
            res = np.flip(self.content, 1)

    def edges(self):
        upper = self.npbin(self.content[0])
        lower = self.npbin(self.content[-1])
        right = self.npbin(self.content[:,-1])
        left = self.npbin(self.content[:,0])
        return [upper, right, lower, left]

    def npbin(self, slice):
        return int(''.join([str(k) for k in slice]), 2)



def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.split('\n\n')
    tiles = {}

    for block in input_data:
        number = int(re.search(r'\d+', block).group(0))
        tile = block.split(':\n')[1]
        tile = np.array([list(line) for line in tile.splitlines()])
        tiles[number] = Tile(number, np.array([x == "#" for x in tile], dtype=np.int8))

    borders = {}
    for n, tile in tiles.items():
        borders[n] = set.union(*[set(tile.edges()) for flip in tile.get_flips()])

    graph = networkx.Graph()
    for i, k in itertools.combinations(borders, 2):
        if len(borders[i] & borders[k]) == 2:
            graph.add_edge(i, j)




def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    pass
