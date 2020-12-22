def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""

    player_1, player_2 = input_data.split('\n\n')
    player_1 = player_1.split('Player 1:\n')[1]
    player_2 = player_2.split('Player 2:\n')[1]

    player_1 = [int(i) for i in player_1.splitlines()]
    player_2 = [int(i) for i in player_2.splitlines()]

    while not(len(player_1) == 0 or len(player_2) == 0):
        top_p1 = player_1[0]
        top_p2 = player_2[0]

        if top_p1 > top_p2:
            player_1.append(player_1.pop(0))
            player_1.append(player_2.pop(0))
        else:
            player_2.append(player_2.pop(0))
            player_2.append(player_1.pop(0))

    winner_deck = player_1 if len(player_1) > 0 else player_2
    result = 0

    for mul, number in enumerate(reversed(winner_deck)):
        result += (mul + 1) * number

    return result



def part_2(input_data: str, recursive:bool=False, player_1:list=None, player_2:list=None):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    if not recursive:
        player_1, player_2 = input_data.split('\n\n')
        player_1 = player_1.split('Player 1:\n')[1]
        player_2 = player_2.split('Player 2:\n')[1]

        player_1 = [int(i) for i in player_1.splitlines()]
        player_2 = [int(i) for i in player_2.splitlines()]

    configurations = []

    while not(len(player_1) == 0 or len(player_2) == 0):
        if player_1 in configurations or player_2 in configurations:
            winner_deck_early = player_1
            break

        else:
            configurations.append(player_1[:])
            configurations.append(player_2[:])

        top_p1 = player_1[0]
        top_p2 = player_2[0]

        # new rule
        if len(player_1) > top_p1 and len(player_2) > top_p2:
            p1_win = part_2(input_data, True, player_1[1:top_p1+1],player_2[1:top_p2+1])
            if p1_win:
                player_1.append(player_1.pop(0))
                player_1.append(player_2.pop(0))
            else:
                player_2.append(player_2.pop(0))
                player_2.append(player_1.pop(0))

        elif top_p1 > top_p2:
            player_1.append(player_1.pop(0))
            player_1.append(player_2.pop(0))
        else:
            player_2.append(player_2.pop(0))
            player_2.append(player_1.pop(0))


    if recursive and len(player_1)>0:
        return True

    if not recursive:
        winner_deck = player_1 if len(player_1) > 0 else player_2
        result = 0

        for mul, number in enumerate(reversed(winner_deck)):
            result += (mul + 1) * number

        return result
