def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    
    input_data = input_data.splitlines()
    input_data = [int(i) for i in input_data]
    input_data.sort()
    
    final_jolt = input_data[-1] + 3
    input_data.append(final_jolt)

    delta = [0,0,0,0]
    last = 0

    for jolt in input_data:
        delta[jolt - last] += 1
        last = jolt

    one_jolt_diff, three_jolt_diff = delta[1], delta[3]

    return one_jolt_diff * three_jolt_diff


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    input_data = [int(i) for i in input_data]
    input_data.sort()

    final_jolt = input_data[-1] + 3
    input_data.append(final_jolt)
    input_data.insert(0,0)

    combos = [0]*input_data[-1]
    combos.insert(0, 1)

    input_data = input_data[1:]

    for c in input_data:
        current = combos[c-3] + combos[c-2] + combos[c-1]
        combos[c] = current

    return combos[-1]
    
    