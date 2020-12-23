def check_sum(preamble_list:list, check_number:int):
    is_valid = False
    for i, num1 in enumerate(preamble_list):
        for k, num2 in enumerate(preamble_list):
            if not i == k:
                if num1 + num2 == check_number:
                    is_valid = True
    if not is_valid:
        return check_number, preamble_list


def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    
    input_data = input_data.splitlines()
    input_data=[int(i) for i in input_data]
    
    preamble_lenght = 25
    i = 0
    number_idx = preamble_lenght
    
    while number_idx < len(input_data):
        current_number = input_data[number_idx]
        result = check_sum(input_data[i:preamble_lenght+i], current_number)

        if result is not None:
            return result[0]

        number_idx += 1
        i += 1


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    invalid_number = part_1(input_data)

    input_data = input_data.splitlines()
    input_data=[int(i) for i in input_data]
    
    preamble_lenght = 2

    # i, k are indices of the first and second number
    for i in range(0, len(input_data)):

        for k in range(i + preamble_lenght, len(input_data)):

            if sum(input_data[i:k]) == invalid_number:

                return max(input_data[i:k]) + min(input_data[i:k])
