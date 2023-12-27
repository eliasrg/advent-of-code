wins = []
with open('input.in') as f:
    for line in f:
        winning, numbers = [
            list(map(int, section.split()))
            for section in ' '.join(line.split()[2:]).split('|')
        ]
        winning = frozenset(winning)
        wins.append(sum(1 for n in numbers if n in winning))

part1_total = sum(2**(w - 1) for w in wins if w != 0)

copies = [1] * len(wins)
for i, w in enumerate(wins):
    if w == 0: continue
    for j in range(i + 1, i + w + 1):
        copies[j] += copies[i]

part2_total = sum(copies)

print(f"Part 1: {part1_total}")
print(f"Part 2: {part2_total}")
