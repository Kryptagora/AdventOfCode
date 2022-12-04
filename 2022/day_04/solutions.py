def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    
    input_data = input_data.splitlines()
    overlaps = 0

    for ranges in input_data:
        ranges = ranges.split(",")
        if range_check(ranges[0], ranges[1]):
            overlaps += 1
        elif range_check(ranges[1], ranges[0]):
            overlaps += 1

    return(overlaps)



def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""
    
    input_data = input_data.splitlines()
    overlaps = 0

    for ranges in input_data:
        ranges = ranges.split(",")
        overlaps += count_overlaps(ranges[0], ranges[1])
    
    return(overlaps)


def range_check(range1, range2):
    """Check if two ranges overlap. range1, 2 has format 2-4"""
    range1 = [int(range1.split("-")[0]), int(range1.split("-")[1])]
    range2 = [int(range2.split("-")[0]), int(range2.split("-")[1])]
    if range1[0] <= range2[0] and range1[1] >= range2[1]:
        return True
    else:
        return False

def count_overlaps(range1, range2):
    """Retruns 1 if range overlaps. range1, 2 has format 2-4"""
    range1 = range(int(range1.split("-")[0]), int(range1.split("-")[1])+1)
    range2 = range(int(range2.split("-")[0]), int(range2.split("-")[1])+1)

    # intersect the sets
    number_set = set(range1).intersection(range2)
    if len(number_set) > 0:
        return 1
    else: return 0