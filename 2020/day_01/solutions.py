def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    numbers = [int(line) for line in input_data.splitlines()]

    for i in numbers:
        for x in numbers:
            if i + x == 2020:
                print(f'Number {i} and {x} add up to 2020. Product: {i*x}')
                return (i*x)

def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    numbers = [int(line) for line in input_data.splitlines()]
    
    for i in numbers:
        for x in numbers:
            for y in numbers:
                if i + x + y == 2020:
                    print(f'Number {i} and {x} and {y} add up to 2020. Product: {i*x*y}')
                    return (i*x*y)