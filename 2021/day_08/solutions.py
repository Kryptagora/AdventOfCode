from collections import Counter

def part_1(input_data: str, part2:bool=False):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = [i.strip().split("|") for i in input_data.splitlines()]

    # the segments as string - to find the output (0-9)
    numbers = "abcefg,cf,acdeg,acdfg,bcdf,abdfg,abdefg,acf,abcdefg,abcdfg"
    numbers_dict = Counter(list(numbers.replace(",", "")))

    mapping = {}
    for idx, text in enumerate(numbers.split(",")):
        mapping[pattern_mapper(text, numbers_dict)] = idx

    result = 0
    for line in input_data:
        process = get_line(line, mapping)
        all_digits = []

        # look into the patterns, if they are one of the numbers, add them
        for digit in process:
            if digit in [1,4,7,8]: all_digits.append(digit)

        if not part2:
            result += len(all_digits)
        else:
            result += int("".join([str(i) for i in process]))


    return result


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    return part_1(input_data, part2=True)


def get_line(line:str = None, mapping:dict=None):
    """Retruns a list of a processed line"""
    occurences = Counter(list(line[0].strip().replace(" ", "")))
    outputs = line[1].strip()
    final = [mapping[pattern_mapper(i, occurences)] for i in outputs.split(" ")]

    return final


def pattern_mapper(text:str=None, occurences:dict=None):
    return tuple(sorted([occurences[i] for i in text]))
