def part_1(input_data: str, part_2:bool=False):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    
    input_data = input_data.splitlines()

    # store rope in a list (head and tail)
    rope = [0 for x in range(10)]
    # set of individual lists
    visited = [set([x]) for x in rope]

    # directions (complex)
    directions = {'L':+1, 'R':-1, 'D':1j, 'U':-1j}
    
    for line in input_data:
        direction, step = line.split()

        for _ in range(int(step)):
            rope[0] += directions[direction]

            for i in range(1, 10):
                # compare to prev distance
                distance = rope[i-1] - rope[i]
                if abs(distance) >= 2:
                    rope[i] += sign(distance)
                    # add to set
                    visited[i].add(rope[i])

    if not part_2: return len(visited[1])
    else: return len(visited[9])


def part_2(input_data: str):
    """Return second solution of puzzle."""
    return part_1(input_data, part_2=True)


def sign(x):
    """Return sign of complex number"""
    return complex((x.real > 0) - (x.real < 0), (x.imag > 0) - (x.imag < 0))
