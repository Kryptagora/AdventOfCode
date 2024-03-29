from importlib import import_module
from aocd.models import Puzzle

from fire import Fire

def solve(day, year='2022', submit=True):
    part_1 = import_module(f'{year}.day_{str(day).zfill(2)}.solutions')
    part_2 = import_module(f'{year}.day_{str(day).zfill(2)}.solutions')
    part_1 = getattr(part_1, 'part_1')
    part_2 = getattr(part_2, 'part_2')
    puzzle = Puzzle(int(year), int(day))
    answer_a = part_1(puzzle.input_data)
    answer_b = part_2(puzzle.input_data)
    if submit:
        puzzle.answer_a = answer_a
        puzzle.answer_b = answer_b

if __name__ == "__main__":
    Fire(solve)
