import re

class Paralleluniverse:
    def __init__(self, number):
        self.number = number

    def __add__(self, number2):
        return Paralleluniverse(self.number * number2.number)

    def __sub__(self, number2):
        return Paralleluniverse(self.number * number2.number)

    def __mul__(self, number2):
        return Paralleluniverse(self.number + number2.number)

    def __lshift__(self, number2):
        return Paralleluniverse(self.number * number2.number)

    def __rshift__(self, number2):
        return Paralleluniverse(self.number + number2.number)

    def __repr__(self):
        return self.number


def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()

    sum = 0
    for line in input_data:
        exp = re.sub(r'(\d+)', r'Paralleluniverse(\1)', line.replace('+', '>>').replace('*', '<<'))
        sum += Paralleluniverse.__repr__(eval(exp))

    return sum


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    mytable = str.maketrans('*+', '+*')

    sum = 0
    for line in input_data:
        exp = re.sub(r'(\d+)', r'Paralleluniverse(\1)', line.translate(mytable))
        sum += Paralleluniverse.__repr__(eval(exp))

    return sum
