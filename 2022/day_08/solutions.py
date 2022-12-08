import numpy as np


def part_1(input_data: str, mode="normal"):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    trees = np.array([[int(i) for i in line] for line in input_data])

    visible_matrix = np.zeros(trees.shape)

    # rotate trough the views
    for _ in range(4):
        for idx, row in enumerate(trees[1:-1]):
            scan_trees(row, visible_matrix, idx)

        visible_matrix, trees = np.rot90(visible_matrix), np.rot90(trees)

    outside = (trees.shape[0])*2 + (trees.shape[1] -2)*2

    # take the sum, ignore outside
    inside_sum = int(np.sum(visible_matrix[1:-1, 1:-1]))
    if mode=="map": return visible_matrix

    return(inside_sum + outside)


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""
    #input_data= "30373\n25512\n65332\n28549\n35390"
    

    input_data = input_data.splitlines()
    trees = np.array([[int(i) for i in line] for line in input_data])
    scores = np.ones(trees.shape, dtype=np.int64)

    # rotate trough the grid
    for _ in range(4):
        for x, y in np.ndindex(trees.shape):   
            lower = [t < trees[x,y] for t in trees[x,y+1:]]
            scores[x,y] *= lower.index(0) + 1 if not all(lower) else len(lower)

        scores = np.rot90(scores)

    return scores.max()



def scan_trees(row:np.array, visible_matrix:np.array, tree_row:int, column:bool=False):
    """Scans and retruns number of visible trees in 1D array"""
    base_tree = row[0]
    if tree_row < 0: 
        shift = -2 
    else: shift = 1

    for idx, tree in enumerate(row[1:]):
        if tree > base_tree:
            visible_matrix[tree_row+shift, idx+shift] = 1
            base_tree = tree