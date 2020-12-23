from sympy.ntheory.modular import crt

def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    depart = int(input_data[0])
    busses = []

    for bus in input_data[1].split(','):
        if not bus == 'x':
            busses.append(int(bus))

    curr = 0
    while True:
        found = None

        for bus in busses:
            if (depart + curr) % bus == 0:
                found = bus

        if found is not None:
            return found*curr

        curr += 1



def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    busses = []

    for bus in input_data[1].split(','):
        if bus == 'x':
            busses.append(None)
        else:
            busses.append(int(bus))


    mod_list, time_diff = [], []

    for i, bus in enumerate(busses):
        if bus:
            mod_list.append(bus)
            time_diff.append(bus - i)

    solved_mods = crt(mod_list, time_diff)[0]

    return solved_mods
