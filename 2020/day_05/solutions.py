def part_1(input_data: str, return_all:bool=False):
    """Return first solution of puzzle."""
    # Make empty testcases run for convencience.
    if input_data == "": return ""
    input_data = input_data.splitlines()

    seat_ids = []
    for line in input_data:
        row_index = [i for i in range(128)]
        column_index = [k for k in range(8)]


        for letter in line[:7]:
            splitpoint = len(row_index)//2
            if letter == 'F':
                row_index = row_index[:splitpoint]
            else:
                row_index = row_index[splitpoint:]

        for letter in line[7:]:
            splitpoint = len(column_index)//2
            if letter == 'R':
                column_index = column_index[splitpoint:]
            else:
                column_index = column_index[:splitpoint]


        seat_ids.append((row_index[0]*8) + column_index[0])
    
    if return_all:
        return max(seat_ids), seat_ids
    
    return max(seat_ids)


def part_2(input_data: str):
    """Return second solution of puzzle."""
    # Make empty testcases run for convencience.
    if input_data == "": return ""
    
    max_id, all_ids = part_1(input_data, return_all=True)
    all_ids.sort()
    differences = []

    for i in range(len(all_ids)-1):
        differences.append(all_ids[i+1]-all_ids[i])
    
    for i, diff in enumerate(differences):
        if diff > 1:
            seat = all_ids[i] + 1 

    return seat
