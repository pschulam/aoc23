def part1(data):
    hs = parse_histories(data)
    total = 0
    for h in hs:
        ds = deltas(h)
        total += predict(ds)
    return total


def part2(data):
    hs = parse_histories(data)
    total = 0
    for h in hs:
        ds = deltas(h)
        total += predict2(ds)
    return total


def predict(ds):
    p = 0
    for d in ds[::-1]:
        p += d[-1]
    return p


def predict2(ds):
    p = 0
    for d in ds[::-1]:
        p = d[0] - p
    return p


def deltas(xs):
    ds = []
    while not all(x == 0 for x in xs):
        ds.append(xs)
        xs = diff(xs)
    return ds


def diff(xs):
    return [x - y for y, x in zip(xs, xs[1:])]


def parse_histories(data):
    hs = []
    for line in data.strip().split("\n"):
        h = list(map(int, line.strip().split()))
        hs.append(h)
    return hs


if __name__ == "__main__":
    import sys
    data = sys.stdin.read()
    print(part1(data))
    print(part2(data))