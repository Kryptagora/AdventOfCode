def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = [int(i) for i in input_data.splitlines()]

    counter = 0
    prev_mesaurement = None
    for mesaurement in input_data:
        if prev_mesaurement is None:
            prev_mesaurement = mesaurement
            continue

        if mesaurement > prev_mesaurement:
            counter += 1

        prev_mesaurement = mesaurement

    return counter


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = [int(i) for i in input_data.splitlines()]

    i = 0
    counter = 0

    while i < len(input_data)-2:
        print(sum(input_data[i:i+3]))
        if sum(input_data[i+1:i+4]) > sum(input_data[i:i+3]):
            counter += 1
        i += 1

    return counter
