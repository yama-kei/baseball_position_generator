import copy
import random
from datetime import datetime


def dedupe_and_remove_empty(listobj):
    result = []
    [result.append(item) for item in listobj if item not in result and item != '']
    return result

def generate_positions(positions, players, innings, norandomize, keeporder):
    """
    This function returns tuple of players (batting order) and map (dictionary)
    consisting of positions (key) and corresponding players for all innings (list as value)
    list of positions, players are given
    positions are kept for the first inning if norandomize option is set
    batting order is preserved if keeporder option is set
    """
    random.seed(datetime.now().timestamp())
    players = dedupe_and_remove_empty(players)
    positions = dedupe_and_remove_empty(positions)
    fieldingpos = {pos:[] for pos in positions}
    fielding_players = copy.deepcopy(players)
    available_positions = positions[:len(fielding_players)]
    if not norandomize:
        # deep randomization
        random.shuffle(fielding_players)
        random.shuffle(available_positions)
    for i in range(innings):
        for c, pos in enumerate(available_positions):
            fieldingpos[pos].append(fielding_players[c])
        fielding_players.append(fielding_players.pop(0))
    # Randomize batting order
    if not keeporder:
        random.shuffle(players)
    return (players, fieldingpos)
