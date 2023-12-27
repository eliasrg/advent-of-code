from collections import defaultdict
import re

with open('input.in') as f:
    lines = f.readlines()

def part1():
    total = 0
    for line in lines:
        digits = list(filter(str.isnumeric, line))
        total += 10 * int(digits[0]) + int(digits[-1])

    return total

def part2():
    digit_vals = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    def get_digit_val(s):
        return digit_vals[s] if s in digit_vals else int(s)

    reverse_digits = {k[::-1] for k in digit_vals}

    pattern = re.compile(r'\d|' + '|'.join(digit_vals.keys()))
    reverse_pattern = re.compile(r'\d|' + '|'.join(reverse_digits))

    total = 0
    for line in lines:
        first = pattern.search(line).group(0)
        last = reverse_pattern.search(line[::-1]).group(0)[::-1]
        total += 10 * get_digit_val(first) + get_digit_val(last)

    return total

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
