from itertools import product

def get_bin(number, n=36):
    return format(number, 'b').zfill(n)

def write(value, mask):
    pos = 0
    result = list(value)
    for m in mask:

        if m == '0':
            result[pos] = '0'
        elif m == '1':
            result[pos] = '1'

        pos += 1

    return ''.join(result)


def write_v2(value, mask):
    pos = 0
    result = list(value)
    results = []

    for m in mask:
        if m == '1':
            result[pos] = '1'
        elif m == 'X':
            result[pos] = 'X'
        pos += 1


    indices = [i for i, c in enumerate(result) if c == 'X']

    for t in product('01', repeat = len(indices)):
        for i, c in zip(indices, t):
            result[i] = c
        results.append(''.join(result))

    return results


def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    bitmask = input_data[0].split(' = ')[1]
    zeros = get_bin(0)
    memory = {}

    for instruction in input_data[1:]:
        cmd = instruction.split(' = ')[0]

        if cmd == 'mask':
            bitmask = instruction.split(' = ')[1]

        else:
            value = get_bin(int(instruction.split(' = ')[1]))
            adress = int(instruction.split('[')[1].split(']')[0])

            memory[adress] = write(value, bitmask)

    sum = 0
    for bin in memory.values():
        sum += int(bin, 2)

    return sum




def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    bitmask = input_data[0].split(' = ')[1]
    memory = {}

    for instruction in input_data[1:]:
        cmd = instruction.split(' = ')[0]

        if cmd == 'mask':
            bitmask = instruction.split(' = ')[1]

        else:
            value = get_bin(int(instruction.split(' = ')[1]))
            adress = get_bin(int(instruction.split('[')[1].split(']')[0]))

            bin_adresses = write_v2(adress, bitmask)

            for adress in bin_adresses:
                memory[int(adress, 2)] = value


    sum = 0
    for bin in memory.values():
        sum += int(bin, 2)

    return sum
