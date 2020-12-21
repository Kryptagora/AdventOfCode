from bidict import bidict
import re

def part_1(input_data: str, mode:str='regular'):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    ingredients = {}
    found = bidict()
    all_names = []

    for line in input_data:
        allergens = re.findall(r'(?<=contains )[^.]*', line)
        allergens = (allergens[0])[:-1]

        names = [n for n in line.split(' (')[0].split(' ')]
        all_names += names

        for allergen in allergens.split(', '):
            if allergen not in ingredients.keys():
                ingredients[allergen] = set(names)
            else:
                ingredients[allergen] &= set(names)


    while ingredients:
        for allergen, names in ingredients.items():
            if len(names) == 1:
                break
        else:
            break
        [name] = names
        found[allergen] = name

        for names in ingredients.values():
            names -= {name}

    if mode == 'regular':
        return sum(i not in found.inv for i in all_names)
    else:
        return found


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    found = part_1(input_data=input_data, mode='found')
    keys = ",".join(sorted(found.inv, key=found.inv.get))

    return keys
