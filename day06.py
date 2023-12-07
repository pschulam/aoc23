"""
For each race, we have the total time of the race and the longest distance.

The total distance traveled for a race with t seconds and button pushed for p ms
d = (t - p) * p

This is a quadratic equation in p:
d = -1 * p**2 + t * p

We match the current record r when
r = -1 * p**2 + t * p

Equivalently
0 = -1 * p**2 + t * p - r

To figure out the range of values for p where we beat the record holder,
we need to find the roots and take all integer values between the roots
(the coefficient on the p**2 term is negative, so the function increases
between the roots).

We can solve for the roots using the quadratic equation:
p1 = (-t + math.sqrt(t**2 - 4*r)) / (-2)
p2 = (-t - math.sqrt(t**2 - 4*r)) / (-2)

"""
import math


def part1(data):
    races = parse_races(data)
    product = 1
    for t, d_best in races:
        strategies = [p for p in range(t + 1) if (t - p) * p > d_best]
        product *= len(strategies)
    return product


def part2(data):
    time, dist = parse_race2(data)
    a, b, c = -1, time, -dist
    sq = math.sqrt(b**2 - 4*a*c)
    p1, p2 = sorted([(-b + sq) / (2*a), (-b - sq) / (2*a)])
    return math.floor(p2) - math.ceil(p1) + 1


def parse_races(data):
    time_str, dist_str, *_ = data.strip().split("\n")
    times = list(map(int, time_str.strip().split()[1:]))
    dists = list(map(int, dist_str.strip().split()[1:]))
    return list(zip(times, dists))


def parse_race2(data):
    time_str, dist_str, *_ = data.strip().split("\n")
    time = int("".join(time_str.strip().split()[1:]))
    dist = int("".join(dist_str.strip().split()[1:]))
    return time, dist


if __name__ == "__main__":
    import sys
    data = sys.stdin.read()
    print(part1(data))
    print(part2(data))