def move(cur_corrdinates:list, direction:str, value:int):

    if direction == 'E':
        cur_corrdinates[0] += value

    elif direction == 'W':
        cur_corrdinates[0] -= value

    elif direction == 'N':
        cur_corrdinates[1] += value

    elif direction == 'S':
        cur_corrdinates[1] -= value

    return cur_corrdinates


def move_realtive(ship_corrdinates:list, waypoint:list, direction:str, value:int):

    if direction == 'E':
        waypoint[0] += value

    elif direction == 'W':
        waypoint[0] -= value

    elif direction == 'N':
        waypoint[1] += value

    elif direction == 'S':
        waypoint[1] -= value

    elif direction == 'F':
        move_by = [i*value for i in waypoint]
        ship_corrdinates = [x+y for x,y in zip(ship_corrdinates, move_by)]

    return waypoint, ship_corrdinates


def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()

    start = [10, 1]
    cur_corrdinates = [10, 1]
    directions = ['N', 'E', 'S', 'W']
    cur_direction = 1


    for command in input_data:
        action, value = command[:1], int(command[1:])

        if action == 'R':
            for turn in range(0, value, 90):
                cur_direction = (cur_direction + 1) % 4

        elif action == 'L':
            for turn in range(0, value, 90):
                cur_direction = (cur_direction - 1) % 4

        if action == 'F':
            cur_corrdinates = move(cur_corrdinates, directions[cur_direction], value)
        else:
            cur_corrdinates = move(cur_corrdinates, action, value)

    x_way = abs(cur_corrdinates[0] - start[0])
    y_way = abs(cur_corrdinates[1] - start[1])

    return x_way + y_way




def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()

    waypoint = [10, 1]
    ship_corrdinates = [0,0]
    directions = ['N', 'E', 'S', 'W']
    cur_direction = 1


    for command in input_data:
        action, value = command[:1], int(command[1:])

        if action == 'R':
            for turn in range(0, value, 90):
                waypoint = [waypoint[1], waypoint[0]*(-1)]

        elif action == 'L':
            for turn in range(0, value, 90):
                waypoint = [waypoint[1]*(-1), waypoint[0]]

        else:
            waypoint, ship_corrdinates = move_realtive(ship_corrdinates, waypoint, action, value)


    x_way = abs(ship_corrdinates[0])
    y_way = abs(ship_corrdinates[1])

    return x_way + y_way
