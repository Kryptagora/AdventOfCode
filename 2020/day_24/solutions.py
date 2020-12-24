from tqdm import tqdm

def adjacent(gamefield, position, directions):
    for d in directions.values():
        yield position + d


def part_1(input_data: str, regular:bool=True):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.replace('e','e ')
    input_data = input_data.replace('w','w ')
    input_data = input_data.splitlines()

    gamefield = {}
    directions = {'e': 2, 'se': 1-1j, 'sw': -1-1j, 'w': -2, 'nw':-1+1j, 'ne':1+1j}

    for line in input_data:
        line = line.split()
        tile = 0
        for x in line:
            tile += directions[x]

        gamefield[tile] = 1 - gamefield.get(tile,0)

    if regular:
        return sum(gamefield.values())
    else:
        return gamefield, directions

def part_2(input_data: str):
    """Return second solution of puzzle."""
    gamefield, directions = part_1(input_data, False)
    steps = 100

    for _ in tqdm(range(steps), desc="Part 2"):
        adjacent_set = {x for i in gamefield for x in adjacent(gamefield, i, directions)}
        black_tiles = set(gamefield.keys()).union(adjacent_set)
        grid = {}

        for i in black_tiles:
            grid[i] = sum(gamefield.get(x, 0) for x in adjacent(gamefield, i, directions))

        for i,s in grid.items():
            if s == 2 or (gamefield.get(i, 0) and s == 1):
                gamefield[i] = True
            else:
                gamefield[i] = False

    return sum(gamefield.values())
