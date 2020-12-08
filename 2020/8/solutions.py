def check_infinite(input_data:str, change_idx:int, jump_mode:bool):
    termination = 0
    idx = 0
    visited = []
    accumulator  = 0
    changed = False

    while termination < len(input_data)*2:

        if idx == len(input_data):
            return True, idx, accumulator

        curr_command, curr_value = input_data[idx].split()
        curr_value = int(curr_value)
           
        if curr_command == 'jmp':

            if not changed and jump_mode and change_idx == idx:

                visited.append(idx)
                idx += 1
                changed = True

            else:
                visited.append(idx)
                idx += curr_value


        if curr_command == 'nop':

            if not changed and not jump_mode and change_idx == idx:

                visited.append(idx)
                idx += curr_value
                changed = True

            else:
                visited.append(idx)
                idx += 1

        if curr_command == 'acc':
            visited.append(idx)
            accumulator += curr_value
            idx += 1
        
        termination += 1

    return False, None, None

def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    
    input_data = input_data.splitlines()
    visited = []
    idx = 0
    accumulator  = 0

    while True:
        curr_command, curr_value = input_data[idx].split()
        curr_value = int(curr_value)

        if idx in visited:
            return accumulator
        
        if curr_command == 'nop':
            visited.append(idx)
            idx += 1
        
        elif curr_command == 'acc':
            visited.append(idx)
            accumulator += curr_value
            idx += 1

        elif curr_command == 'jmp':
            visited.append(idx)
            idx += curr_value
        

            

def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()

    visited = []
    idx = 0
    tryied_changing_idx = []
    changed = False

    accumulator  = 0

    for change_idx in range(len(input_data)):
        
        # Change jmp to nop
        found, idx, acc = check_infinite(input_data, change_idx, True)
        if found:
            print(f"Found! Change 'jmp' -> 'nop' in index {idx}. Accumulator = {acc}")
            return acc
        
        # Change nop to jmp
        found, idx, acc = check_infinite(input_data, change_idx, False)
        if found:
            print(f"Found! Change 'nop' -> 'jmp' in index {idx}. Accumulator = {acc}")
            return acc
        



    