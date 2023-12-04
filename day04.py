def part1(data):
    total = 0
    for line in data.strip().split("\n"):
        _, winning, played = parse_card(line)
        overlap = set(winning) & set(played)
        if overlap:
            total += 2**(len(overlap) - 1)
    return total


def part2(data):
    cards = [parse_card(line) for line in data.strip().split("\n")]
    counts = [1] * len(cards)
    total = 0
    for i, (_, winning, played) in enumerate(cards):
        c = counts[i]
        overlap = set(winning) & set(played)
        total += c
        if overlap:
            n = len(overlap)
            for j in range(n):
                counts[i + j + 1] += c
    return total


def parse_card(line):
    head, content = line.strip().split(":")
    _, game_id = head.strip().split()
    winning, played = content.strip().split("|")
    winning = list(map(int, winning.strip().split()))
    played = list(map(int, played.strip().split()))
    return int(game_id), winning, played


if __name__ == "__main__":
    import sys
    data = sys.stdin.read()
    print(part1(data))
    print(part2(data))
