from itertools import repeat
from math import prod

def memoize(f):
    cache = dict()

    def memo_f(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return memo_f

def solve(row, groups):
    # Number of arrangements using exactly g groups in row[:i]
    # if allowed to start a group at row[i] (no # at row[i-1])
    @memoize
    def rec(i, g):
        if g == len(groups):
            return int('#' not in row[i:])
        elif i >= len(row):
            return 0

        ans = 0

        # Don't use a group
        if row[i] != '#':
            ans += rec(i + 1, g)

        # Use a group
        if row[i] != '.':
            group_end = i + groups[g]
            if (group_end <= len(row)
                and '.' not in row[i:group_end]
                and (group_end == len(row) or row[group_end] != '#')):
                ans += rec(group_end + 1, g + 1)

        return ans

    return rec(0, 0)

part1_total = part2_total = 0
with open('input.in') as f:
    for row, group_str in map(str.split, f.readlines()):
        groups = tuple(map(int, group_str.split(',')))
        part1_total += solve(row, groups)
        part2_total += solve('?'.join(repeat(row, 5)), groups * 5)

print(f"Part 1: {part1_total}")
print(f"Part 2: {part2_total}")
