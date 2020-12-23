def part_1(input_data: str, move_right:int=3, move_down:int=1):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    slopes = input_data.splitlines()
    tree_count = 0
    move_increment = move_right
    
    for slope, i in zip(slopes, range(0, len(slopes), 1)):
        if i == 0:
            continue
        
        if i % move_down == 0:

            if slope[move_right%len(slope)] == '#':
                tree_count += 1

            move_right += move_increment
        
    return tree_count

    

def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    slopes = input_data.splitlines()
    score = 1

    for i in [1,3,5,7]:
        score *= part_1(input_data, move_right=i)
    score *= part_1(input_data, move_right=1, move_down=2)

    return score