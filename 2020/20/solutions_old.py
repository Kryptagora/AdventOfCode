import numpy as np
import re
from tqdm import tqdm


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

    def edges(self):
        edges = {}
        edges['left'] = ''.join(self.content[:,0])
        edges['right'] = ''.join(self.content[:,-1])
        edges['upper'] = ''.join(self.content[0])
        edges['lower'] = ''.join(self.content[-1])
        return edges

    def allign_with(self, array_2, mode):
        if array_2.count_rotations > 4:
            array_2._reset_rotations_()
            return None

        if mode == 'R':
            if self.edges()['right'] == array_2.edges()['left']:
                array_2._reset_rotations_()
                return array_2
            else:
                return self.allign_with(array_2.rotate(), mode='R')

        elif mode == 'L':
            if self.edges()['lower'] == array_2.edges()['upper']:
                array_2._reset_rotations_()
                return array_2
            else:
                return self.allign_with(array_2.rotate(), mode='L')


def _hardreset_(tile_dict:dict):
    for _, elem in tile_dict.items():
        elem._reset_rotations_()

def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    # with open('2020/20/in', 'r') as fh:
    #     input_data = fh.read()

    input_data = input_data.split('\n\n')

    tiles = {}
    for block in input_data:
        number = int(re.search(r'\d+', block).group(0))
        tile = block.split(':\n')[1]
        tile = np.array([list(line) for line in tile.splitlines()])
        tiles[number] = Tile(number, tile)

    len_cube = int(np.sqrt(len(tiles)))
    puzzle = np.zeros(shape=(len_cube, len_cube), dtype=object)
    corridinates = [0,0]
    current_tile = None
    for step in tqdm(puzzle):
        found = False
        if current_tile is None:
            tile = next(iter(tiles.values()))

        for _, fit_me in tiles.items():
            if found:
                break
            # ignore the same tile
            if _ == tile.id_number:
                continue

            # when the tile gets rotated 180 degrees, the order changes.
            fit_me_edges_reversed = [x[::-1] for x in fit_me.edges().values()]
            for _ in range(4):

                for _ in range(4):
                    # first check if the edges match without flipping

                    if corridinates[1] < len_cube-1:
                        if tile.edges()['right'] in fit_me.edges().values() or tile.edges()['right'] in fit_me_edges_reversed:
                            # check if the edges match and if so, allign the tile
                            next_tile = tile.allign_with(array_2=fit_me, mode='R')
                            if next_tile is not None:
                                corridinates[1] += 1
                                puzzle[corridinates] = next_tile.id_number
                                current_tile = next_tile
                                found = True
                                break
                            else:
                                _hardreset_(tiles)

                    else:
                        if tile.edges()['lower'] in fit_me.edges().values() or tile.edges()['lower'] in fit_me_edges_reversed:
                            next_tile = tile.allign_with(array_2=fit_me, mode='U')

                            if next_tile is not None:
                                corridinates[1] = 0
                                corridinates[0] += 1
                                puzzle[corridinates] = next_tile.id_number
                                current_tile = next_tile
                                found = True
                                break
                            else:
                                _hardreset_(tiles)

                    # no match, try to rotate the flipped original tile
                    fit_me.rotate()


                # now try it with flipping the tiles beforehand
                fit_me.flip()
                if found: break
                for _ in range(4):
                    # first check if the edges match without flipping

                    #if [a in fit_me.edges().items() for a in tile.edges().items()]:
                    if corridinates[1] < len_cube-1:
                        if tile.edges()['right'] in fit_me.edges().values() or tile.edges()['right'] in fit_me_edges_reversed:
                            # check if the edges match and if so, allign the tile
                            next_tile = tile.allign_with(array_2=fit_me, mode='R')
                            if next_tile is not None:
                                corridinates[1] += 1
                                puzzle[corridinates] = next_tile.id_number
                                current_tile = next_tile
                                found = True
                                break
                            else:
                                _hardreset_(tiles)

                    else:
                        if tile.edges()['lower'] in fit_me.edges().values() or tile.edges()['lower'] in fit_me_edges_reversed:
                            next_tile = tile.allign_with(array_2=fit_me, mode='U')
                            if next_tile is not None:
                                corridinates[1] = 0
                                corridinates[0] += 1
                                puzzle[corridinates] = next_tile.id_number
                                current_tile = next_tile
                                found = True
                                break
                            else:
                                _hardreset_(tiles)

                    # no match, try to rotate the flipped original tile
                    fit_me.rotate()

                #rotate the fixed tile and check again
                tile.rotate()

            fit_me._reset_rotations_()
        _hardreset_(tiles)
    print(puzzle)





def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    pass
