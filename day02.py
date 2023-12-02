import re
from collections import defaultdict


def part1(data):
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    total = 0
    for line in data.strip().split("\n"):
        game_id, results = parse_line(line)
        invalid = any(any(r[k] > bag[k] for k in r) for r in results)
        if not invalid:
            total += game_id
    return total


def part2(data):
    total = 0
    for line in data.strip().split("\n"):
        _, results = parse_line(line)
        max_obs = defaultdict(int)
        for result in results:
            for key in result:
                max_obs[key] = max(max_obs[key], result[key])
        power = 1
        for v in max_obs.values():
            power *= v
        total += power
    return total


def parse_line(line):
    game_str, results_str = line.strip().split(":")
    game_id = int(re.match(r"^Game (\d+)", game_str).group(1))
    results = []
    for result_str in results_str.split(";"):
        counts = {}
        for count_str in result_str.strip().split(","):
            value, key = count_str.strip().split()
            counts[key] = int(value)
        results.append(counts)
    return game_id, results


if __name__ == "__main__":
    import sys
    data = sys.stdin.read()
    print(part1(data))
    print(part2(data))
