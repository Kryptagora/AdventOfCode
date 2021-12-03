import numpy as np

def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    
    input_data = [list(row) for row in input_data.splitlines()]
    input_data = np.array(input_data, dtype=np.int64)
    binary = ""

    for c in input_data.T:
        zero, one = np.count_nonzero(c == 0), np.count_nonzero(c == 1)
        if zero > one:
            binary += "0"
        else:
            binary += "1"
    
    gamma = int(binary, 2)
    delta = int(binary.replace("1", "2").replace("0", "1").replace("2", "0"), 2)

    return gamma * delta


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = [list(row) for row in input_data.splitlines()]
    input_data = np.array(input_data, dtype=np.int64)
    input_data2 = np.copy(input_data)

    end = False
    current_idx = 0

    while not end:
        # when only one element is left
        if input_data.shape[0] == 1:
            break

        c = input_data.T[current_idx]
        zero, one = np.count_nonzero(c == 0), np.count_nonzero(c == 1)
        mfd = []

        if zero > one:
            for i, _ in enumerate(input_data):
                if input_data[i][current_idx] == 1:
                    mfd.append(i)
        else:
            for i, _ in enumerate(input_data):
                if input_data[i][current_idx] == 0:
                    mfd.append(i)

        input_data = np.delete(input_data, mfd, 0)
        current_idx += 1

    oxygen_rating = int("".join([str(x) for x in input_data[0]]), 2)

    # scrubber rating --
    end = False
    current_idx = 0

    while not end:
        if input_data2.shape[0] == 1:
            break

        c = input_data2.T[current_idx]
        zero, one = np.count_nonzero(c == 0), np.count_nonzero(c == 1)
        mfd = []

        if zero > one:
            for i, _ in enumerate(input_data2):
                if input_data2[i][current_idx] == 0:
                    mfd.append(i)
        else:
            for i, _ in enumerate(input_data2):
                if input_data2[i][current_idx] == 1:
                    mfd.append(i)

        input_data2 = np.delete(input_data2, mfd, 0)
        current_idx += 1

    scrubber_rating = int("".join([str(x) for x in input_data2[0]]), 2)

    return scrubber_rating * oxygen_rating


