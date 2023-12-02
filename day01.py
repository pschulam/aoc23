import re

DIGITS = {str(i) for i in range(10)}
DIGITS_RE = re.compile(r"[1-9]|one|two|three|four|five|six|seven|eight|nine")


def part1(data):
    total = 0
    for line in data.strip().split("\n"):
        digits = [c for c in line.strip() if c in DIGITS]
        total += int(digits[0] + digits[-1])
    return total


def part2(data):
    total = 0
    for line in data.strip().split("\n"):
        digits = scan_for_digits(line)
        total += int(digit2int(digits[0]) + digit2int(digits[-1]))
    return total


def scan_for_digits(line):
    pos = 0
    digits = []
    while True:
        m = DIGITS_RE.search(line, pos=pos)
        if m is None:
            break
        digits.append(digit2int(m.group(0)))
        pos = m.start() + 1
    return digits


def digit2int(s):
    if re.match(r"[1-9]", s):
        return s
    if re.match(r"one|two|three|four|five|six|seven|eight|nine", s):
        return {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }[s]
    raise ValueError(f"not a valid digit: {s}")


if __name__ == "__main__":
    import sys
    data = sys.stdin.read()
    print(part1(data))
    print(part2(data))
