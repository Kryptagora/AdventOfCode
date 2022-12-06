def part_1(input_data: str, message_length: int=4):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    
    i = 0
    signal = 0
    while i < len(input_data):
        if check_string_repetition(input_data[i:i+message_length]):
            signal = i+message_length
            break 
        i += 1

    return signal


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""
    
    return part_1(input_data, 14)



def check_string_repetition(text: str):
    """Check if string has repeating characters."""
    return len(set(text)) == len(text)

