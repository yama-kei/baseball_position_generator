import copy
import random


def dedupe_and_remove_empty(listobj):
    result = []
    [result.append(item) for item in listobj if item not in result and item != '']
    return result

def generate_positions(positions, players, innings, norandomize, keeporder):
    players = dedupe_and_remove_empty(players)
    positions = dedupe_and_remove_empty(positions)
    fieldingpos = {pos:[] for pos in positions}
    fielding = copy.deepcopy(players)
    available = positions[:len(fielding)]
    if norandomize:
        for c, pos in enumerate(available):
            fieldingpos[pos].append(fielding[c])
        innings -= 1
    random.shuffle(available)
    if not keeporder:
        random.shuffle(players)
    for i in range(innings):
        for c, pos in enumerate(available):
            fieldingpos[pos].append(fielding[c])
        fielding.append(fielding.pop(0))
    return (players, fieldingpos)
