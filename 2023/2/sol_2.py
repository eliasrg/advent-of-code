from math import prod

with open('input.in') as f:
    lines = f.readlines()

bounds = {'red': 12, 'green': 13, 'blue': 14}

part1_answer = part2_answer = 0
for i, line in enumerate(lines):
    possible = True
    min_bounds = {'red': 0, 'green': 0, 'blue': 0}

    words = line.split()[2:]
    for num, col in zip(words[::2], words[1::2]):
        num = int(num)
        col = col.replace(',', '').replace(';', '')
        if num > bounds[col]:
            possible = False
        min_bounds[col] = max(min_bounds[col], num)

    if possible: part1_answer += i + 1
    part2_answer += prod(min_bounds.values())

print(f"Part 1: {part1_answer}")
print(f"Part 2: {part2_answer}")
