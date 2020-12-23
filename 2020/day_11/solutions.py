import numpy as np

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 'X')
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
    return vector



def part_1(input_data: str):
    """Iterate over the field via convoluions."""
    if input_data == "": return ""

    seat_grid = [[x for x in line] for line in input_data.splitlines()]
    seat_grid = np.asarray(seat_grid)
    seat_grid = np.pad(seat_grid, 1, pad_with)

    seat_grid_old = np.zeros(shape=seat_grid.shape, dtype=np.str)

    end_pos = [seat_grid.shape[0] - 3, seat_grid.shape[1] - 3]

    while not (seat_grid == seat_grid_old).all():
        current_pos = [0,0]
        seat_grid_old = np.copy(seat_grid)

        while not current_pos == end_pos:
            current_subgrid = seat_grid_old[current_pos[0]:current_pos[0]+3,\
                                        current_pos[1]:current_pos[1]+3]


            if seat_grid_old[current_pos[0]+1][current_pos[1]+1] == 'L' and np.sum(current_subgrid=='#') == 0:
                seat_grid[current_pos[0]+1][current_pos[1]+1] = '#'


            elif seat_grid_old[current_pos[0]+1][current_pos[1]+1] == '#' and np.sum(current_subgrid=='#')-1 >= 4:
                seat_grid[current_pos[0]+1][current_pos[1]+1] = 'L'


            # update position
            if current_pos[1] + 1 == seat_grid.shape[1] - 1:
                current_pos[0] += 1
                current_pos[1] = 0
            else:
                current_pos[1] += 1

    return np.sum(seat_grid=='#')


def part_2(input_data: str):
    """Doing the same thing as in part one, but expanding the view of the passengers
    on the seat incremently. The indexing is differnt, here it starts wit 1,1 instead
    of 0,0."""
    if input_data == "": return ""


    seat_grid = [[x for x in line] for line in input_data.splitlines()]
    seat_grid = np.asarray(seat_grid)
    seat_grid = np.pad(seat_grid, 1, pad_with)

    seat_grid_old = np.zeros(shape=seat_grid.shape, dtype=np.str)

    end_pos = [seat_grid.shape[0] - 1, seat_grid.shape[1] - 1]

    while not (seat_grid == seat_grid_old).all():
        current_pos = [1,1]

        seat_grid_old = np.copy(seat_grid)

        while not current_pos == end_pos:
            if not (seat_grid[current_pos[0]][current_pos[1]] == 'L' or seat_grid[current_pos[0]][current_pos[1]] == '#'):
                # update position in case if there is no one
                if current_pos[1] == seat_grid.shape[1] - 1:
                    current_pos[0] += 1
                    current_pos[1] = 0
                else:
                    current_pos[1] += 1

                continue


            directions = [None]*8
            # 0 1 2
            # 3 L 4
            # 5 6 7
            for i in range(8):
                view_stop = False
                expand = 1

                while not view_stop:
                    if i == 0:
                        if directions[i] is None:
                            if seat_grid_old[current_pos[0]-expand][current_pos[1]-expand] == 'X':
                                directions[i] = 'X'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]-expand][current_pos[1]-expand] == '#':
                                directions[i] = '#'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]-expand][current_pos[1]-expand] == 'L':
                                directions[i] = 'L'
                                view_stop = True

                            elif seat_grid_old[current_pos[0]-expand][current_pos[1]-expand] == '.':
                                expand += 1

                    elif i == 1:
                        if directions[i] is None:
                            if seat_grid_old[current_pos[0]-expand][current_pos[1]] == 'X':
                                directions[i] = 'X'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]-expand][current_pos[1]] == '#':
                                directions[i] = '#'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]-expand][current_pos[1]] == 'L':
                                directions[i] = 'L'
                                view_stop = True

                            elif seat_grid_old[current_pos[0]-expand][current_pos[1]] == '.':
                                expand += 1

                    elif i == 2:
                        if directions[i] is None:
                            if seat_grid_old[current_pos[0]-expand][current_pos[1]+expand] == 'X':
                                directions[i] = 'X'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]-expand][current_pos[1]+expand] == '#':
                                directions[i] = '#'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]-expand][current_pos[1]+expand] == 'L':
                                directions[i] = 'L'
                                view_stop = True

                            elif seat_grid_old[current_pos[0]-expand][current_pos[1]+expand] == '.':
                                expand += 1

                    elif i == 3:
                        if directions[i] is None:
                            if seat_grid_old[current_pos[0]][current_pos[1]-expand] == 'X':
                                directions[i] = 'X'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]][current_pos[1]-expand] == '#':
                                directions[i] = '#'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]][current_pos[1]-expand] == 'L':
                                directions[i] = 'L'
                                view_stop = True

                            elif seat_grid_old[current_pos[0]][current_pos[1]-expand] == '.':
                                expand += 1

                    elif i == 4:
                        if directions[i] is None:
                            if seat_grid_old[current_pos[0]][current_pos[1]+expand] == 'X':
                                directions[i] = 'X'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]][current_pos[1]+expand] == '#':
                                directions[i] = '#'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]][current_pos[1]+expand] == 'L':
                                directions[i] = 'L'
                                view_stop = True

                            elif seat_grid_old[current_pos[0]][current_pos[1]+expand] == '.':
                                expand += 1


                    elif i == 5:
                        if directions[i] is None:
                            if seat_grid_old[current_pos[0]+expand][current_pos[1]-expand] == 'X':
                                directions[i] = 'X'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]+expand][current_pos[1]-expand] == '#':
                                directions[i] = '#'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]+expand][current_pos[1]-expand] == 'L':
                                directions[i] = 'L'
                                view_stop = True

                            elif seat_grid_old[current_pos[0]+expand][current_pos[1]-expand] == '.':
                                expand += 1

                    elif i == 6:
                        if directions[i] is None:
                            if seat_grid_old[current_pos[0]+expand][current_pos[1]] == 'X':
                                directions[i] = 'X'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]+expand][current_pos[1]] == '#':
                                directions[i] = '#'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]+expand][current_pos[1]] == 'L':
                                directions[i] = 'L'
                                view_stop = True

                            elif seat_grid_old[current_pos[0]+expand][current_pos[1]] == '.':
                                expand += 1

                    elif i == 7:
                        if directions[i] is None:
                            if seat_grid_old[current_pos[0]+expand][current_pos[1]+expand] == 'X':
                                directions[i] = 'X'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]+expand][current_pos[1]+expand] == '#':
                                directions[i] = '#'
                                view_stop = True
                            elif seat_grid_old[current_pos[0]+expand][current_pos[1]+expand] == 'L':
                                directions[i] = 'L'
                                view_stop = True

                            elif seat_grid_old[current_pos[0]+expand][current_pos[1]+expand] == '.':
                                expand += 1



            if seat_grid_old[current_pos[0]][current_pos[1]] == 'L' and directions.count('#') == 0:
                seat_grid[current_pos[0]][current_pos[1]] = '#'


            elif seat_grid_old[current_pos[0]][current_pos[1]] == '#' and directions.count('#') >= 5:
                seat_grid[current_pos[0]][current_pos[1]] = 'L'


            # update position
            if current_pos[1] == seat_grid.shape[1] - 2:
                current_pos[0] += 1
                current_pos[1] = 0
            else:
                current_pos[1] += 1


    return np.sum(seat_grid=='#')
