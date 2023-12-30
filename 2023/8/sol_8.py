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

def path_length(pos, goal_end):
    for step, instr in enumerate(cycle(instrs)):
        if pos.endswith(goal_end): break
        pos = network[pos][instr]
    return step

part1_answer = path_length('AAA', 'ZZZ')

# Should not work in general, but apparently works for this input
part2_answer = lcm(*(path_length(start, 'Z')
                     for start in network.keys() if start.endswith('A')))

print(f"Part 1: {part1_answer}")
print(f"Part 2: {part2_answer}")
