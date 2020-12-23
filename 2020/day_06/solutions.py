def part_1(input_data: str):
    """Return first solution of puzzle."""
    # Make empty testcases run for convencience.
    if input_data == "": return ""
    input_data = input_data.split("\n\n")
    final_sum = 0
    
    for group in input_data:
        group = group.replace('\n', "")
        already_answerd = []
        group_sum = 0

        for char in group:
            if char.isalpha() and char.lower() not in already_answerd:
                already_answerd.append(char.lower())
                group_sum += 1
        
        final_sum += group_sum

    return final_sum

        


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""
    input_data = input_data.split("\n\n")
    final_sum = 0
    
    for group in input_data:

        group = group.splitlines()
        intersection = set.intersection(*map(set, list(group)))

        final_sum += len(intersection)


    return final_sum