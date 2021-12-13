import numpy as np

def part_1(input_data: str, part_2:bool=False):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    coordinates, fold = input_data.split("\n\n")
    grid = np.zeros((2000, 2000), dtype=bool)
    max_x, max_y = np.NINF, np.NINF


    # add coords to the grid
    for c in coordinates.split("\n"):
        x, y = int(c.split(",")[0]), int(c.split(",")[1])

        # updadate the arrays later (avoid sparsity)
        if x > max_x: max_x = x
        if y > max_y: max_y = y

        grid[y][x] = True

    # cut off irrelevant parts
    grid = grid[:max_y+1, :max_x+1]

    for fold_cmd in [f for f in fold.split("\n")]:
        if "x" in fold_cmd:
            grid = fold_array(grid, 0, coord=int(fold_cmd.split("=")[1].strip()))

        elif "y" in fold_cmd:
            grid = fold_array(grid, 1, coord=int(fold_cmd.split("=")[1].strip()))

        # part1: only first fold
        if not part_2: break

    if not part_2:
        return(grid.sum().sum())

    else:
        # the output will be printed
        grid_repr(grid)



def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    return(part_1(input_data, part_2=True))


def fold_array(grid:np.array=None, axis:int=0, coord:int=0):
    """Folds array given its axis (x=0, y=1) at the given cooridinate"""
    if axis == 0:
        # split the array along x (vertical)
        original, fold = np.array_split(grid, [coord], axis=1)

        # ignore the dots on the fold line
        fold = fold[:, 1:]

        # flip it
        fold = np.fliplr(fold)

        # add this to the slice of given position
        return original + fold

    elif axis == 1:
        # split the array along y (horizontal)
        original, fold = np.array_split(grid, [coord], axis=0)

        # ignore the dots on the fold line
        fold = fold[1:]

        # flip it
        fold = np.flipud(fold)

        # add this to the slice of given position
        return original + fold


def grid_repr(grid:np.array=None):
    """prints array as AoC String (for debugging) - or for the second task"""
    for i in range(0, grid.shape[0]):

        for j in range(0, grid.shape[1]):
            if grid[i,j]:
                print("█", end="")

            else:
                print(" ", end="")

        print("\n")

    print("\n")
