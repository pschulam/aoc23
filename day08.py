import itertools
import math
import re


def part1(data):
    instrs, transitions_str = data.strip().split("\n\n", maxsplit=1)
    instrs = itertools.cycle(instrs.strip())
    transitions = parse_transitions(transitions_str)
    transition_func = make_transition_func(transitions)
    state = "AAA"
    steps = 0
    while state != "ZZZ":
        instr = next(instrs)
        state = transition_func(state, instr)
        steps += 1
    return steps


def part2(data):
    instrs_str, transition_str = data.strip().split("\n\n", maxsplit=1)
    transitions = parse_transitions(transition_str)
    transition_func = make_transition_func(transitions)
    start = sorted(set(s for s in transitions if s.endswith("A")))
    pathl = {}
    for s in start:
        st = s
        instrs = itertools.cycle(instrs_str)
        steps = 0
        while not s.endswith("Z"):
            instr = next(instrs)
            s = transition_func(s, instr)
            steps += 1
        pathl[st] = steps
    return math.lcm(*list(pathl.values()))


def parse_transitions(transitions_str):
    transitions = {}
    for node in transitions_str.strip().split("\n"):
        match = re.match(r"([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)", node)
        src = match.group(1)
        nb1 = match.group(2)
        nb2 = match.group(3)
        transitions[src] = (nb1, nb2)
    return transitions


def make_transition_func(transitions):
    def transition_func(state, instr):
        return transitions[state][0 if instr == "L" else 1]
    return transition_func


if __name__ == "__main__":
    import sys
    data = sys.stdin.read()
    print(part1(data))
    print(part2(data))