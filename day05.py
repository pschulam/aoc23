import re


def part1(data):
    seeds, mappings = parse_input(data)
    return min(apply_maps(s, mappings) for s in seeds)


def part2(data):
    seeds, mappings = parse_input(data)
    return min(apply_maps_range(zip(seeds[::2], seeds[1::2]), mappings))[0]


def parse_input(data):
    seeds_str, *maps_str = data.strip().split("\n\n")
    seeds = [int(x) for x in re.findall(r"\d+", seeds_str)]
    mappings = []
    for map_str in maps_str:
        mapping = []
        for row in re.findall(r"\d+ \d+ \d+", map_str):
            dst, src, length = map(int, row.split())
            mapping.append((dst, src, length))
        mappings.append(mapping)
    return seeds, mappings


def apply_maps(x, mappings):
    for mapping in mappings:
        x = apply_map(x, mapping)
    return x


def apply_map(x, mapping):
    for d, s, n in mapping:
        if s <= x < s + n:
            return d + (x - s)
    return x


def apply_map_range(s, n, mapping):
    unmatched = [(s, s + n - 1)]
    matched = []
    while unmatched:
        collision = False
        j = unmatched.pop(0)
        for dst, src, length in mapping:
            i = src, src + length - 1
            o, r = collide(i, j)
            if o is not None:
                m = dst + o[0] - src, dst + o[1] - src
                matched.append((m[0], m[1] - m[0] + 1))
                unmatched.extend(r)
                collision = True
        if not collision:
            matched.append((j[0], j[1] - j[0] + 1))
    return matched


def apply_maps_range(seeds, mappings):
    for mapping in mappings:
        seeds = [pair for s, n in seeds for pair in apply_map_range(s, n, mapping)]
    return seeds


def collide(i, j):
    """Return the part of j that falls within i and the parts that don't."""
    if i[1] < j[0] or j[1] < i[0]: # no overlap at all
        return None, [j]
    if i[0] <= j[0] and j[1] <= i[1]: # i contains j
        return j, []
    if j[0] <= i[0] and i[1] <= j[1]: # j contains i
        remainder = []
        if j[0] < i[0]:
            remainder.append((j[0], i[0] - 1))
        if i[1] < j[1]:
            remainder.append((i[1] + 1, j[1]))
        return i, remainder
    if i[0] < j[0] and j[0] <= i[1] <= j[1]: # i right overlaps with j left
        overlap = j[0], i[1]
        remainder = [] if i[1] == j[1] else [(i[1] + 1, j[1])]
        return overlap, remainder
    if j[0] < i[0] and i[0] <= j[1] <= i[1]: # j right overlaps with i left
        overlap = i[0], j[1]
        remainder = [(j[0], i[0] - 1)]
        return overlap, remainder
    raise RuntimeError("should never get here")


if __name__ == "__main__":
    import sys
    data = sys.stdin.read()
    print(part1(data))
    print(part2(data))
