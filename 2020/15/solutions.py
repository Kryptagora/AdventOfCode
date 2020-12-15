def find_last_occurence(history:list, element:int):
    indices = [None, None]
    for i in reversed(range(len(history))):
        if history[i] == element and indices[1] is None:
            indices[1] = i
        elif history[i] == element and indices[0] is None:
            indices[0] = i
        if None not in indices:
            return indices


def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.split(',')
    history = [int(i) for i in input_data]
    current_round = len(history)
    new_number = None

    while current_round < 2020:

        if new_number in history[:-1]:
            # return index of last occurences
            indices = find_last_occurence(history, new_number)
            new_number = abs(indices[0]-indices[1])

        else:
            new_number = 0

        history.append(new_number)
        current_round += 1

    return new_number


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.split(',')
    input_data = [int(i) for i in input_data]
    history = {}

    current_round = 0
    last_number = None


    while current_round < len(input_data):
        new_number = input_data[current_round]

        history[last_number] = current_round - 1
        last_number = new_number
        current_round +=1


    while current_round < 30000000:
        if last_number in history.keys():
            new_number = (current_round-1)-history[last_number]

        else:
            new_number = 0

        history[last_number] = current_round - 1
        last_number = new_number
        current_round +=1

    return new_number
