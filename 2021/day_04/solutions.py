import numpy as np

def part_1(input_data: str, part2: bool=False):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    # nice trick to parse data fast
    n, *b = input_data.split("\n\n")

    # 1D Array of Numebrs
    n = np.loadtxt(n.split(',')).reshape(-1, 1, 1, 1)

    # All boards
    b = np.loadtxt(b).reshape(1, -1, 5, 5)

    # 4D matrix contains each board after each draw - counts cummulative draws
    m = (n == b).cumsum(0)

    # get the scores
    scores = (n * b * (1 - m)).sum((2, 3))

    # find winning board with argmax
    w = (m.all(2) | m.all(3)).any(2).argmax(0)

    # get the result
    d_scores = scores[w].diagonal()
    if not part2:
        return int(d_scores[w.argsort()[[0]]][0])
    else:
        return int(d_scores[w.argsort()[[-1]]][0])


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    # same as before - but now take te last score from the list!
    return part_1(input_data, part2=True)
