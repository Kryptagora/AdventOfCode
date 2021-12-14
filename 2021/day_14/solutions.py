from collections import Counter

def part_1(input_data: str, steps:int=10):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    input_data = [line.strip() for line in input_data.splitlines()]

    # starting point
    template = input_data[0]

    polymers = Counter(template)
    pairs = Counter([x+y for (x, y) in zip(template, template[1:])])

    insertion_rules = {}
    for line in input_data[2:]:
        x,y,z = line[0],line[1],line[-1]
        insertion_rules[x+y] = z

    for i in range(steps):
        old = pairs.copy()
        for (x,y),z in insertion_rules.items():
            count = old[x+y]

            # decrease count of original pair
            pairs[x+y] -= count

            # increase count of replacement pairs
            pairs[x+z] += count
            pairs[z+y] += count

            # increase count of new char
            polymers[z] += count

    # subtract last common from most common
    most_common = polymers.most_common()[0][1]
    last_common = polymers.most_common()[-1][1]

    return most_common - last_common


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    return part_1(input_data, steps=40)
