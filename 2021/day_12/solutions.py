from collections import defaultdict
adj = defaultdict(list)

def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    for line in input_data.splitlines():
        p1, p2 = line.strip().split("-")

        # set the adjecent caves
        adj[p1].append(p2)
        adj[p2].append(p1)


    return search(visit_twice=False)

def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    return search_2()


def search(cave:str="start", seen:dict={'start'}, visit_twice:bool=False):
    """Traverses the caves and returns the count of paths (given that we can
    only visit one XOR twice from the specification) """
    if cave == 'end':
        return 1

    # counter for paths
    count = 0

    for n in adj[cave]:
        if n.islower():
            if n not in seen:
                count += search(n, seen | {n}, visit_twice)

            elif visit_twice and n not in ['start', 'end']:
                count += search(n, seen | {n}, visit_twice)

        else:
            count += search(n, seen, visit_twice)

    return count


def search_2(cave: str="start", seen:set=set(), double:str=None):
    """Sone twerks to the first search, since it dumpes the core."""
    if cave == 'end':
        return 1

    if cave == "start" and seen:
        return 0

    if cave.islower() and cave in seen:
        if double is None:
            double = cave
        else:
            return 0

    seen = seen | {cave}
    count = 0
    for c in adj[cave]:
        count += search_2(c, seen, double)

    return count
