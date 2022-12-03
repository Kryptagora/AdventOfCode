import string

def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    
    input_data = input_data.splitlines()

    alphabet= list(string.ascii_lowercase) + list(string.ascii_uppercase)
    scores = {alphabet[i]: i+1 for i in range(len(alphabet))}

    priory_sum = 0
    for line in input_data:
        half = len(line)//2
        matches = list(set(line[:half]) & set(line[half:]))
        for match in matches:
            priory_sum += scores[match]

    return priory_sum


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""
    
    input_data = input_data.splitlines()

    alphabet= list(string.ascii_lowercase) + list(string.ascii_uppercase)
    scores = {alphabet[i]: i+1 for i in range(len(alphabet))}

    priory_sum = 0
    idx = 0
    while idx < len(input_data):
        intersect = list(set(input_data[idx]) & set(input_data[idx + 1]) & set(input_data[idx + 2]))
        for match in intersect:
            priory_sum += scores[match]
        
        idx += 3

    return priory_sum
        

