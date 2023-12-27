from collections import defaultdict
from math import prod
import re

with open('input.in') as f:
    rows = list(map(str.strip, f.readlines()))

part1_total = 0
star_numbers = defaultdict(list)
for r, row in enumerate(rows):
    for match in re.finditer(r'\d+', row):
        number = int(match.group(0))
        part_number = False
        for i in range(max(0, r - 1), min(len(rows), r + 2)):
            for j in range(max(0, match.start() - 1),
                           min(len(row), match.end() + 1)):
                if re.match(r'[^0-9.]', rows[i][j]):
                    part_number = True
                if rows[i][j] == '*':
                    star_numbers[i, j].append(number)

        if part_number:
            part1_total += number

part2_total = sum(prod(nums)
                  for nums in star_numbers.values()
                  if len(nums) == 2)

print(f"Part 1: {part1_total}")
print(f"Part 2: {part2_total}")
