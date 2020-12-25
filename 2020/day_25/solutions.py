from tqdm import tqdm

def transform(subject_number:int, loop_size:int, goal:int):
    val = 1
    for i in range(1,loop_size+1):
        val = val * subject_number
        val = val % 20201227
        if val == goal:
            return i, val
    return val

def codebreak(subject_number:int, max_loop_size:int, goal:int):
    i = 1
    val = 1
    while i < max_loop_size:
        val = val * subject_number
        val = val % 20201227
        if val == goal:
            return i, val
        i += 1
    return None

def part_1(input_data: str):
    """Breaks the loop size while increasing depth."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    pub_key_1, pub_key_2 = int(input_data[0]), int(input_data[1])
    max_loop_size = 50000000

    loop_size_1, num1 = codebreak(7, max_loop_size, pub_key_1)
    loop_size_2, num2 = codebreak(7, max_loop_size, pub_key_2)
    encryption_key = transform(pub_key_1, loop_size_2, -1)

    return encryption_key




def part_2(input_data: str):
    """happy new year"""
