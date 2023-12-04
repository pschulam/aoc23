import re
from collections import defaultdict


class Stream:
    def __init__(self, buffer):
        self.buffer = buffer
        self.i = 0
        self.l = 0
        self.c = 0
        self.n = len(buffer)

    def peek(self, forward=0):
        i = self.i + forward
        return self.buffer[i] if i < self.n else None

    def take(self):
        c = self.peek()
        self.i += 1
        if c == "\n":
            self.l += 1
            self.c = 0
        else:
            self.c += 1
        return c


def is_digit(c):
    return re.match(r"\d", c) is not None


def parse_schematic(data):
    stream = Stream(data.strip())
    symbols = {}
    part_nums = {}
    while stream.peek() is not None:
        c = stream.peek()
        if c == "." or c == "\n":
            stream.take()
            continue
        if is_digit(c):
            i = stream.l
            j = stream.c
            n = 0
            while stream.peek(n) is not None and is_digit(stream.peek(n)):
                n += 1
            part_num = "".join(stream.take() for _ in range(n))
            part_nums[(i, j)] = part_num
        else:
            i = stream.l
            j = stream.c
            symbols[(i, j)] = stream.take()
    return symbols, part_nums


def adjacent(si, sj, pi, pj1, pj2):
    if si == pi:
        return sj == (pj1 - 1) or sj == (pj2 + 1)
    if si == (pi - 1) or si == (pi + 1):
        return (pj1 - 1) <= sj <= (pj2 + 1)
    return False


def part1(data):
    symbols, part_nums = parse_schematic(data)
    total = 0
    for (pi, pj1), num in part_nums.items():
        pj2 = pj1 + len(num) - 1
        if any(adjacent(si, sj, pi, pj1, pj2) for (si, sj) in symbols):
            total += int(num)
    return total


def part2(data):
    symbols, part_nums = parse_schematic(data)
    gear_to_parts = defaultdict(list)
    for (si, sj), symb in symbols.items():
        if symb == "*":
            for (pi, pj1), num in part_nums.items():
                pj2 = pj1 + len(num) - 1
                if adjacent(si, sj, pi, pj1, pj2):
                    gear_to_parts[(si, sj)].append(num)
    total = 0
    for (si, sj), parts in gear_to_parts.items():
        if len(parts) == 2:
            n1, n2 = sorted(parts)
            total += int(n1) * int(n2)
    return total


if __name__ == "__main__":
    import sys
    data = sys.stdin.read()
    print(part1(data))
    print(part2(data))
