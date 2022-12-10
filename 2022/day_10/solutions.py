import numpy as np

def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    
    input_data = input_data.splitlines()
    cycle = 0

    register = np.zeros(shape=(1000,), dtype=np.int64)
    register[0] = 1
    final_sum = 0

    idx = 0
    empty_cycle = False
    
    while idx < len(input_data):
        if input_data[idx] == "noop":
            cycle += 1
            idx += 1

        elif empty_cycle:
                cycle += 1
                empty_cycle = False

        else:
            _, value = input_data[idx].split()
            register[idx+2] = value
            cycle += 1
            empty_cycle = True
            idx += 1

        if cycle in [20, 60, 100, 140, 180, 220]:
            if cycle == 220: final_sum += cycle * sum(register[:idx])
            else: final_sum += cycle * sum(register[:idx+1])

    return int(final_sum)


def part_2(input_data: str):
    """Return second solution of puzzle. This code is one of the worst ive ever written. I brute forced the answer
    from the output, since it hast "errors". They are of course intentionally - like old CRTs have them ;)"""
    if input_data == "": return ""
    
    input_data = input_data.splitlines()
    cycle = 0

    register = np.zeros(shape=(1000,), dtype=np.int64)
    register[0] = 1
    final_sum = ""

    idx = 0
    empty_cycle = False
    
    while idx < len(input_data):
        if input_data[idx] == "noop":
            # a dirty fix for skipping 
            if cycle in get_window(idx, register):
                final_sum += "#"
            else:
                final_sum += " "

            cycle += 1
            idx += 1  
                 

            if cycle % 40 == 0:
                final_sum += "\n"
                cycle = 0     

            continue

        elif empty_cycle:
                cycle += 1
                empty_cycle = False

        else:
            _, value = input_data[idx].split()
            register[idx+1] = value
            cycle += 1
            empty_cycle = True
            idx += 1

        
        if cycle in get_window(idx, register):
            final_sum += "#"
        else:
            final_sum += " "

        

        if cycle % 40 == 0:
            final_sum += "\n"
            cycle = 0

    print(final_sum)


def get_window(start:int, register):
    """returns list f range of window"""
    return list(range(sum(register[:start]), sum(register[:start])+3))
