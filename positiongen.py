import random


def generate_positions(positions, players, innings, randomize=True):
    random.shuffle(players)
    fieldingpos = {pos:[] for pos in positions}
    fielding = players[:len(positions)]
    available = positions[:len(fielding)]
    random.shuffle(available)
    for i in range(innings):
        for c, pos in enumerate(available):
            fieldingpos[pos].append(fielding[c])
        fielding.append(fielding.pop(0))
    return (players, fieldingpos)
