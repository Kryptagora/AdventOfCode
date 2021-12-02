def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    
    input_data = [cmd.split(" ") for cmd in input_data.splitlines()]
    h, d = 0, 0

    for cmd in input_data:
        if cmd[0] == "forward":
            h += int(cmd[1])
        elif cmd[0] == "down":
            d += int(cmd[1])
        elif cmd[0] == "up":
            d -= int(cmd[1])

    return h * d


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = [cmd.split(" ") for cmd in input_data.splitlines()]
    h, d, aim = 0, 0, 0

    for cmd in input_data:
        if cmd[0] == "forward":
            h += int(cmd[1])
            d += aim * int(cmd[1])
        elif cmd[0] == "down":
            aim += int(cmd[1])
        elif cmd[0] == "up":
            aim -= int(cmd[1])

    return h * d
