def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    # rock paper scissors
    scores = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    lost_combitations = ["AZ", "CY", "BX"]
    win_combinations = ["AY", "BZ", "CX"]

    score = 0
    for line in input_data:
        score += scores[line.split(" ")[1]]

        if line.replace(" ", "") in lost_combitations:
            score += 0
        elif line.replace(" ", "") in win_combinations:
            score += 6
        else:
            score += 3
        
    return score

def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""
    
    input_data = input_data.splitlines()

    lost_combitations = ["AZ", "CY", "BX"]
    win_combinations = ["AY", "BZ", "CX"]
    draw_combinations = ["AX", "BY", "CZ"]

    new_input = ""
    for line in input_data:
        # lose case 
        if line.split(" ")[1] == "X":
            combination = next(x for x in lost_combitations if x.startswith(line.split(" ")[0]))
        # draw case
        elif line.split(" ")[1] == "Y":
            combination = next(x for x in draw_combinations if x.startswith(line.split(" ")[0]))
        # win case
        elif line.split(" ")[1] == "Z":
            combination = next(x for x in win_combinations if x.startswith(line.split(" ")[0]))

        new_input += combination[0] + " " + combination[1] + "\n"
    

    return( part_1(new_input) )
        