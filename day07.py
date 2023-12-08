import re
from collections import Counter


CARD_TO_RANK  = {c: i for i, c in enumerate("23456789TJQKA")}
CARD_TO_RANK2 = {c: i for i, c in enumerate("J23456789TQKA")}


TYPE_TO_RANK = {
    "FIVE_OF_A_KIND": 6,
    "FOUR_OF_A_KIND": 5,
    "FULL_HOUSE": 4,
    "THREE_OF_A_KIND": 3,
    "TWO_PAIR": 2,
    "ONE_PAIR": 1,
    "HIGH_CARD": 0,
}


def hand_to_type(hand: str):
    coc = Counter(Counter(hand).values())
    if coc == {5: 1}:
        return TYPE_TO_RANK["FIVE_OF_A_KIND"]
    if coc == {1: 1, 4: 1}:
        return TYPE_TO_RANK["FOUR_OF_A_KIND"]
    if coc == {2: 1, 3: 1}:
        return TYPE_TO_RANK["FULL_HOUSE"]
    if coc == {1: 2, 3: 1}:
        return TYPE_TO_RANK["THREE_OF_A_KIND"]
    if coc == {1: 1, 2: 2}:
        return TYPE_TO_RANK["TWO_PAIR"]
    if coc == {1: 3, 2: 1}:
        return TYPE_TO_RANK["ONE_PAIR"]
    if coc == {1: 5}:
        return TYPE_TO_RANK["HIGH_CARD"]
    raise RuntimeError("Should never get here")


def hand_to_type2(hand: str):
    n_jokers = sum(c == "J" for c in hand)
    n_others = len({c for c in hand if c != "J"})
    if n_jokers == 5:
        return TYPE_TO_RANK["FIVE_OF_A_KIND"]
    if n_jokers == 4:
        return TYPE_TO_RANK["FIVE_OF_A_KIND"]
    if n_jokers == 3:
        if n_others == 1:
            return TYPE_TO_RANK["FIVE_OF_A_KIND"]
        else:
            return TYPE_TO_RANK["FOUR_OF_A_KIND"]
    if n_jokers == 2:
        if n_others == 1:
            return TYPE_TO_RANK["FIVE_OF_A_KIND"]
        elif n_others == 2:
            return TYPE_TO_RANK["FOUR_OF_A_KIND"]
        else:
            return TYPE_TO_RANK["THREE_OF_A_KIND"]
    if n_jokers == 1:
        return max(hand_to_type(re.sub(r"J", c, hand)) for c in CARD_TO_RANK2 if c != "J")
    return hand_to_type(hand)


def hand_sort_key(hand: str):
    handt = hand_to_type(hand)
    ranks = [CARD_TO_RANK[c] for c in hand]
    return tuple([handt] + ranks)


def hand_sort_key2(hand: str):
    handt = hand_to_type2(hand)
    ranks = [CARD_TO_RANK2[c] for c in hand]
    return tuple([handt] + ranks)


def part1(data):
    hands = [line.strip().split() for line in data.strip().split("\n")]
    hands = sorted(hands, key=lambda x: hand_sort_key(x[0]))
    total = 0
    for i, (_, bid) in enumerate(hands, start=1):
        total += i * int(bid)
    return total


def part2(data):
    hands = [line.strip().split() for line in data.strip().split("\n")]
    hands = sorted(hands, key=lambda x: hand_sort_key2(x[0]))
    total = 0
    for i, (_, bid) in enumerate(hands, start=1):
        total += i * int(bid)
    return total


if __name__ == "__main__":
    import sys
    data = sys.stdin.read()
    print(part1(data))
    print(part2(data))