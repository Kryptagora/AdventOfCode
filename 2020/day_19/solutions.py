import re

def get_rule(rules_dict:dict, number:int, mode:str='std'):
    """Retruns the pattern according to the given rules"""
    current_rule = rules_dict[number]

    if '"' in current_rule:
        return current_rule[1]

    else:
        subrules = current_rule.split(' | ')
        seq = []
        for sub in subrules:
            numbers = sub.split(' ')
            if mode == 'std':
                seq.append(''.join(get_rule(rules_dict, int(num)) for num in numbers))
            else:
                seq.append(''.join(rule_tunnel(rules_dict, int(num)) for num in numbers))

        pattern = '(?:' + '|'.join(seq) + ')'
        return pattern


def rule_tunnel(rules_dict:dict, number:int, max_depth:int=80):
    """Tunnels original input and checks if the rules need to be modified"""
    if number == 8:
        return get_rule(rules_dict, 42, mode='tunnel') + '+'

    elif number == 11:
        a = get_rule(rules_dict, 42, mode='tunnel')
        b = get_rule(rules_dict, 31, mode='tunnel')
        new_pattern = '(?:' + '|'.join(f'{a}{{{i}}}{b}{{{i}}}' for i in range(1, max_depth)) + ')'
        return new_pattern

    else:
        return get_rule(rules_dict, number, mode='tunnel')


def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    rules, messages = input_data.split("\n\n")
    rules, messages = rules.splitlines(), messages.splitlines()
    rules_dict = {}

    for rule in rules:
        rules_dict[int(rule.split(': ')[0])] = rule.split(': ')[1]


    evaluate = get_rule(rules_dict, 0)
    count = 0
    for message in messages:
        match = re.fullmatch(evaluate, message)
        if match:
            count += 1

    return count


def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    rules, messages = input_data.split("\n\n")
    rules, messages = rules.splitlines(), messages.splitlines()
    rules_dict = {}

    for rule in rules:
        rules_dict[int(rule.split(': ')[0])] = rule.split(': ')[1]

    evaluate = rule_tunnel(rules_dict, 0)
    count = 0
    for message in messages:
        match = re.fullmatch(evaluate, message)
        if match:
            count += 1

    return count
