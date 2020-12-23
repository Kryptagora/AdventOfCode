import re

pattern = r'[1-9]\s*([a-z]\w+ [a-z]\w+){0,2}'
pattern_withnumber = r'([1-9]\s*[a-z]\w+ [a-z]\w+) {0,2}'


def search_all(input_data:str, color:str, path:list):

    for line in input_data:
        if line.split()[0] + " " + line.split()[1] == color:
            matches = re.findall(pattern, line)

            if 'shiny gold' in matches:
                return True
            else:
                for c in matches:
                    if c not in path:
                        path.append(c)
                        if search_all(input_data, c, path):
                            return True

                    
                return False

def find_color(input_data:str, color:str):

    for line in input_data:
        if line.split()[0] + " " + line.split()[1] == color:
            matches = re.findall(pattern_withnumber, line)
            return matches
            

def count_bags(input_data:str, start_bag:str, bag_elements:str):
    count = 0
    if len(bag_elements) != 0:

        for bag_element in bag_elements:
            num, col = bag_element.split(" ", 1)
            count += int(num)
            count += int(bag_element[0]) * count_bags(input_data, col, find_color(input_data, col) )
        return count

    else:
        return 0
            

    

def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    input_data = input_data.splitlines()
    golden_bags = 0

    for rule in input_data:
        current_bag = rule.split()[0] + " " + rule.split()[1]
        current_bag_elements = re.findall(pattern, rule)
        path = []

        if 'shiny gold' in current_bag_elements:
                golden_bags += 1
                continue
        
        for c in current_bag_elements:
            if search_all(input_data, c, path):
                golden_bags += 1
                break

    return golden_bags



def part_2(input_data: str):
    """Return second solution of puzzle."""
    # Make empty testcases run for convencience.
    if input_data == "": return ""

    input_data = input_data.splitlines()

    for rule in input_data:

        current_bag = rule.split()[0] + " " + rule.split()[1]

        if current_bag == 'shiny gold':
            current_bag_elements = re.findall(pattern_withnumber, rule)
 
            return count_bags(input_data, 'shiny gold', current_bag_elements)
