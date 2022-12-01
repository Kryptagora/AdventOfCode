versions = []

def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    table = {
      "0" : "0000",
      "1" : "0001",
      "2" : "0010",
      "3" : "0011",
      "4" : "0100",
      "5" : "0101",
      "6" : "0110",
      "7" : "0111",
      "8" : "1000",
      "9" : "1001",
      "A" : "1010",
      "B" : "1011",
      "C" : "1100",
      "D" : "1101",
      "E" : "1110",
      "F" : "1111",
    }

    input_data = [i for i in input_data.strip()]
    input_data = "".join([table[i] for i in list(input_data)])

    packet_version = int(input_data[:3], 2)
    type_id = int(input_data[3:6], 2)



def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    pass


def parse_packet(input_data:str=None, idx:int=0):
    """Given input data (must be binary string), returns parsed packet"""
    if "1" not in input_data:
        return idx

    if idx >= len(input_data):
        return idx


    versions = list()
    version_num = input_data[idx : idx + 3]
    type_id = input_data[idx + 3 : idx + 6]

    versions.append(int(version_num, 2))

    if type_id == "100":
        end_idx, val = parse_literal_groups(input_data, idx + 6)
        return end_idx, val

    length_type = input_data[idx + 6]
    subvalues = []
    parsed_idx = None
    if length_type == "0":
        total_length = int(input_data[idx + 7 : idx + 22], 2)
        parsed_idx = idx + 22
        while parsed_idx < idx + 22 + total_length:
            parsed_idx, val = parse_packet(input_data, parsed_idx)
            subvalues.append(val)
    elif length_type == "1":
        packet_count = int(input_data[idx + 7 : idx + 18], 2)
        parsed_idx = idx + 18
        for i in range(packet_count):
            parsed_idx, val = parse_packet(input_data, parsed_idx)
            subvalues.append(val)
    else:
        raise ValueError()
    assert parsed_idx is not None

    val = None
    if type_id == "000":
        val = sum(subvalues)
    elif type_id == "001":
        val = 1
        for subvalue in subvalues:
            val *= subvalue
    elif type_id == "010":
        val = min(subvalues)
    elif type_id == "011":
        val = max(subvalues)
    elif type_id == "101":
        val = 1 if subvalues[0] > subvalues[1] else 0
    elif type_id == "110":
        val = 1 if subvalues[0] < subvalues[1] else 0
    elif type_id == "111":
        val = 1 if subvalues[0] == subvalues[1] else 0

    return parsed_idx, val


def parse_literal_groups(bin_sub_str, idx):
    sub_str_idx = idx
    group = bin_sub_str[sub_str_idx : sub_str_idx + 5]
    bin_val = ""
    while True:
        bin_val += group[1:]
        if group[0] == "0":
            break
        sub_str_idx += 5
        group = bin_sub_str[sub_str_idx : sub_str_idx + 5]
    literal_value = int(bin_val, 2)
    return sub_str_idx + 5, literal_value


input_data = utils.get_input(day=16).strip()
input_data = utils.hex_to_bin(input_data)
idx, val = parse_packet(input_data, 0)

print(f"Part 1: {sum(versions)}")
print(f"Part 2: {val}")



###--------------------------------------------------------
#For refrence:
import utils


versions = []


def parse_packet(input_data, idx):
    if "1" not in input_data:
        return idx
    if idx >= len(input_data):
        return idx

    version_num = input_data[idx : idx + 3]
    type_id = input_data[idx + 3 : idx + 6]

    versions.append(int(version_num, 2))

    if type_id == "100":
        end_idx, val = parse_literal_groups(input_data, idx + 6)
        return end_idx, val

    length_type = input_data[idx + 6]
    subvalues = []
    parsed_idx = None
    if length_type == "0":
        total_length = int(input_data[idx + 7 : idx + 22], 2)
        parsed_idx = idx + 22
        while parsed_idx < idx + 22 + total_length:
            parsed_idx, val = parse_packet(input_data, parsed_idx)
            subvalues.append(val)
    elif length_type == "1":
        packet_count = int(input_data[idx + 7 : idx + 18], 2)
        parsed_idx = idx + 18
        for i in range(packet_count):
            parsed_idx, val = parse_packet(input_data, parsed_idx)
            subvalues.append(val)
    else:
        raise ValueError()
    assert parsed_idx is not None

    val = None
    if type_id == "000":
        val = sum(subvalues)
    elif type_id == "001":
        val = 1
        for subvalue in subvalues:
            val *= subvalue
    elif type_id == "010":
        val = min(subvalues)
    elif type_id == "011":
        val = max(subvalues)
    elif type_id == "101":
        val = 1 if subvalues[0] > subvalues[1] else 0
    elif type_id == "110":
        val = 1 if subvalues[0] < subvalues[1] else 0
    elif type_id == "111":
        val = 1 if subvalues[0] == subvalues[1] else 0

    return parsed_idx, val


def parse_literal_groups(bin_sub_str, idx):
    sub_str_idx = idx
    group = bin_sub_str[sub_str_idx : sub_str_idx + 5]
    bin_val = ""
    while True:
        bin_val += group[1:]
        if group[0] == "0":
            break
        sub_str_idx += 5
        group = bin_sub_str[sub_str_idx : sub_str_idx + 5]
    literal_value = int(bin_val, 2)
    return sub_str_idx + 5, literal_value


input_data = utils.get_input(day=16).strip()
input_data = utils.hex_to_bin(input_data)
idx, val = parse_packet(input_data, 0)

print(f"Part 1: {sum(versions)}")
print(f"Part 2: {val}")
