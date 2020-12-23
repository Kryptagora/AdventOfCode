def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    data_aray = input_data.splitlines()
    correct_count = 0

    for line in data_aray:
        line = line.split()
        minval, maxval = line[0].split("-")

        minval, maxval = int(minval), int(maxval)

        letter = list(line[1])[0]

        pwd = line[2]

        if not ((pwd.count(letter) < minval) or (pwd.count(letter) > maxval)):
            correct_count += 1
        
    return correct_count

def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    data_aray = input_data.splitlines()
    correct_count = 0

    for line in data_aray:
        line = line.split()
        first, second = line[0].split("-")

        first, second = int(first), int(second)

        letter = list(line[1])[0]

        pwd = line[2]

        if (pwd[first-1] == letter) ^ (pwd[second-1] == letter):
            correct_count += 1
        
    return correct_count