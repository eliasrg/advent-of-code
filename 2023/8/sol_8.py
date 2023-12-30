from itertools import cycle
from math import lcm

with open('input.in') as f:
    instrs = ['LR'.index(char) for char in f.readline().strip()]
    f.readline()
    network = {
        src: (left, right)
        for line in f
        for src, left, right in [''.join(filter(
                lambda char: char.isalnum() or char.isspace(), line)).split()]
    }

def part1():
    pos = 'AAA'
    for step, instr in enumerate(cycle(instrs)):
        if pos == 'ZZZ': break
        pos = network[pos][instr]
    return step

def part2():
    def path_length(start):
        pos = start
        for step, instr in enumerate(cycle(instrs)):
            if pos.endswith('Z'): break
            pos = network[pos][instr]
        return step

    # Should not work in general, but apparently works for this input
    return lcm(*(path_length(start)
                 for start in network.keys() if start.endswith('A')))

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
