import numpy as np
import re

def part_1(input_data: str, inverted:int=1):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    """    with open("2022/day_05/sample.txt", "r") as f:
        input_data = f.read()"""
    
    array_data, move_instructions = input_data.split("\n\n")
    chest_array = []
    # create array
    for idx, line in enumerate(array_data.splitlines()):
        if line[1].startswith("1"):
            break

        i = 0
        row = []
        while i < len(line)-1:
            row.append(line[i+1])
            i += 4
        chest_array.append(row)

    # get moves (quantity, start, end)
    moves = []
    for line in move_instructions.splitlines():
        moves.append([int(x) for x in re.findall(r'\d+', line)])


    # convert to np and make it easier to work with (transpose and flip) 
    chest_array = np.flip(np.array(chest_array).T, axis=1)

    chest_array = extend_arrays(chest_array, 1000)

    # iterate over moves and move chests
    for move in moves:
        chests_to_move, new_chest_line = get_chests(chest_array[move[1]-1], move[0])

        # update chest array
        chest_array[move[1]-1] = new_chest_line

        # insert chests into new line
        inserted_chest_array = insert_chests(chest_array[move[2]-1], chests_to_move, inverted=inverted)

        # update chest array
        chest_array[move[2]-1] = inserted_chest_array

    # get last elements from chetsts 
    last_elements = ""
    for line in chest_array:
        last_elements += line[line != " "][-1]

    return last_elements
   

def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""
    
    return part_1(input_data, inverted=-1)




def extend_arrays(array: np.array, size: int):
    """Adds size to array in 2d array collection"""
    return np.pad(array, ((0, 0),(0, size)), 'constant', constant_values=" ")


def get_chests(array: np.array, number: int):
    """Takes number of elements from array that are not empty from the end"""
    chests_to_move = array[array != " "][-number:]
    
    # remove them from array
    num_elements = len(array[array != " "])

    # concartenate 
    new_array = np.concatenate((
        array[:num_elements-number], 
        np.array([" " for i in range(len(array) - num_elements + number)])
        ))
    
    return chests_to_move, new_array


def insert_chests(array: np.array, chests: np.array, inverted:int=1):
    """Inserts chests into array. returns updated array"""
    # insert array where array is not " " 
    num_elements = len(array[array != " "])
    
    new_array = np.concatenate((
        array[:num_elements],
        # CrateMover 9001 just inverts chests insertion
        chests[::-1*inverted],
        np.array([" " for i in range(len(array)-len(chests)-num_elements)])
        ))

    return new_array

    



