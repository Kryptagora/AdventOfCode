import numpy as np
import re
from tqdm import tqdm

def part_1(input_data: str, return_valid_tickets:bool=False):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    ranges, my_ticket, nearby = [line for line in input_data.split("\n\n")]
    range_list = re.findall('[0-9]+-[0-9]+', ranges)

    invalid_sum = 0
    valid_tickets = []
    nearby = nearby.split(':\n')[1].splitlines()
    for ticket in nearby:
        ticket = [int(i) for i in ticket.split(",")]
        valid_ticket = True
        for number in ticket:
            in_range = False
            for sin_range in range_list:
                if number in range(int((sin_range.split('-')[0])), int((sin_range.split('-')[1]))+1):
                    in_range = True

            if not in_range:
                invalid_sum += number
                valid_ticket = False

        if valid_ticket:
            valid_tickets.append(ticket)

    if not return_valid_tickets:
        return invalid_sum
    else:
        return valid_tickets




def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    ranges, my_ticket, _ = [line for line in input_data.split("\n\n")]
    my_ticket = my_ticket.split(':\n')[1]
    my_ticket = [int(i) for i  in my_ticket.split(',')]

    valid_tickets = part_1(input_data=input_data, return_valid_tickets=True)
    valid_tickets.append(my_ticket)
    valid_tickets = np.array(valid_tickets)

    range_dict = {}
    column_element_dict = {}

    for line in ranges.splitlines():
        range_dict[line.split(':')[0]] = re.findall('[0-9]+-[0-9]+', line)


    pbar = tqdm(total = len(column_element_dict))
    while len(column_element_dict) < 20:

        for entry, range_tuple in range_dict.items():
            range_1 = range(int(range_tuple[0].split('-')[0]), int(range_tuple[0].split('-')[1])+1)
            range_2 = range(int(range_tuple[1].split('-')[0]), int(range_tuple[1].split('-')[1])+1)
            possibilities = []

            for i, column in enumerate(valid_tickets.T):
                in_range = True

                if i in column_element_dict.keys():
                    continue

                for elem in column:
                    if not (elem in range_1 or elem in range_2):
                        in_range = False

                if in_range:
                    possibilities.append(i)

            if len(possibilities) == 1:
                column_element_dict[possibilities[0]] = entry
                pbar.update(1)

    depart_number = 1
    for i, label in column_element_dict.items():
        if "departure" in label:
            depart_number *= my_ticket[i]

    return depart_number
