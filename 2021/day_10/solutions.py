def part_1(input_data: str, part_2 = False):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = [line.strip() for line in input_data.splitlines()]

    symbols = {')': '(', ']': '[', '}': '{', '>': '<'}
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    points_alt = {'(': 1, '[': 2, '{': 3, '<': 4}
    score = 0
    scores = []

    for line in input_data:
        stack = []

        for c in list(line):
            if c in list(symbols.values()):
                stack.append(c)

            elif stack.pop() != symbols[c]:
                score += points[c]

            elif not stack:
                score += points[c]

    return score


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = [line.strip() for line in input_data.splitlines()]

    symbols = {')': '(', ']': '[', '}': '{', '>': '<'}
    points_alt = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = []

    for line in input_data:
        stack = []

        for c in list(line):
            if c in list(symbols.values()):
                stack.append(c)

            elif stack.pop() != symbols[c]:
                stack = None
                break

            elif not stack:
                stack = None
                break

        if stack is not None:
            subscore = 0

            for c in reversed(stack):
                subscore = 5 * subscore + points_alt[c]

            scores.append(subscore)

    middle_score = int(sorted(scores)[int(len(scores)/2)])

    return middle_score
