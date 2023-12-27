from math import prod, sqrt, floor, ceil

input_file = 'input.in'

# Hold button for t ms; go a distance t * (time - t).

def part1():
    with open(input_file) as f:
        times, records = [list(map(int, line.split()[1:]))
                          for line in f.readlines()]

    return prod(
        sum(1 for t in range(time + 1)
            if t * (time - t) > record)
        for time, record in zip(times, records))

def part2():
    with open(input_file) as f:
        time, record = (int(''.join(line.split()[1:]))
                        for line in f.readlines())

    # Solve t**2 - t*time + record < 0
    low = ceil(time/2 - sqrt(time**2/4 - record))
    high = floor(time/2 + sqrt(time**2/4 - record))
    return high - low + 1

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
