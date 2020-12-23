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

    def rotate(self):
        self.content = np.rot90(self.content)
        return self


    def flip(self):
        self.content = np.flip(self.content)
        return self

    def get_flips(self):
        res = self.content
        for f in range(2):
            for i in range(4):
                yield res
                res = np.rot90(res)
            res = np.flip(self.content, 1)

    def get_flips_external(self, external):
        res = external
        for f in range(2):
            for i in range(4):
                yield res
                res = np.rot90(res)
            res = np.flip(external, 1)

    def edges(self):
        upper = self.npbin(self.content[0])
        lower = self.npbin(self.content[-1])
        right = self.npbin(self.content[:,-1])
        left = self.npbin(self.content[:,0])
        return [upper, right, lower, left]

    def get_edge_location(self, loc):
        upper = self.npbin(loc[0])
        lower = self.npbin(loc[-1])
        right = self.npbin(loc[:,-1])
        left = self.npbin(loc[:,0])
        return [upper, right, lower, left]


    def npbin(self, slice):
        return int(''.join([str(k) for k in slice]), 2)


def npbin(slice):
    return int("".join([str(i) for i in slice]), 2)


def get_edges(tile):
    return [npbin(tile[0]), npbin(tile[:, -1]), npbin(tile[-1]), npbin(tile[:, 0])]


def get_flips(tile):
    curr = tile

    for _ in range(2):
        for _ in range(4):
            yield curr
            curr = np.rot90(curr)
        curr = np.flip(tile, 1)


def part_1(input_data: str, mode:str='regular'):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    input_data = input_data.split('\n\n')

    tiles = {}
    borders = {}
    corners = []
    graph = networkx.Graph()

    for block in input_data:
        number = int(re.search(r'\d+', block).group(0))
        tile = block.split(':\n')[1]
        tile = np.array([list(line) for line in tile.splitlines()])
        tiles[number] = Tile(number, np.array([x == "#" for x in tile], dtype=np.int8))
    len_cube = int(np.sqrt(len(tiles)))

    for n, tile in tiles.items():
        borders[n] = set.union(*[set(tile.get_edge_location(flip)) for flip in tile.get_flips()])


    for i, k in tqdm(itertools.combinations(borders, 2)):
        if len(borders[i] & borders[k]) == 2:
            graph.add_edge(i, k)

    for i in graph:
        if len(graph[i]) == 2:
            corners.append(i)

    if mode == 'regular':
        return functools.reduce(operator.mul, corners)
    else:
        return tiles, borders, corners, graph, len_cube



def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""
    tiles, borders, corners, graph, len_cube = part_1(input_data, mode='return')

    new_tiles = {}
    for id, tile in tiles.items():
        new_tiles[id] = tile.content

    tiles = new_tiles

    def external(leaf):
        used = set(tile for tile, _ in grd.values())
        tile, img = grd[leaf]
        border = get_edges(img)
        for x in graph[tile]:
            if x not in used:

                for flip in get_flips(tiles[x]):

                    if get_edges(flip)[0] == border[2]:
                        grd[(leaf[0] + 1, leaf[1])] = (x, flip)
                    if get_edges(flip)[3] == border[1]:
                        grd[(leaf[0], leaf[1] + 1)] = (x, flip)

    for flip in get_flips(tiles[corners[0]]):
        grd = {}
        grd[(0, 0)] = (corners[0], flip)
        external((0, 0))
        if len(grd) == 3:
            break

    for i in range(12):
        for j in range(12):
            external((i, j))

    image = np.concatenate([np.concatenate([grd[i, j][1][1:-1, 1:-1] for j in range(len_cube)], axis=1) for i in range(len_cube)], axis=0)
    with open('2020/20/monster', 'r') as mo:
        monster_file = mo.read()

    monster_file = monster_file.splitlines()
    monster = np.array([[x == "#" for x in line] for line in monster_file], dtype=np.int8)

    for image in tqdm(get_flips(image)):
        count = 0

        for i in range(image.shape[0] - monster.shape[0] + 1):
            for j in range(image.shape[1] - monster.shape[1] + 1):
                check = image[i : i + monster.shape[0], j : j + monster.shape[1]]
                if (check & monster == monster).all():
                    count += 1

        if count:
            break

    entire_puzzle_num = np.sum(image)
    monster_sum = np.sum(monster)

    return int(entire_puzzle_num - count * monster_sum)
