with open('input') as f:
    rows = f.readlines()

cols = list(zip(*rows))

row_lengths, col_lengths = [
    [1 if '#' in line else 2 # Del 2: 1000000
     for line in ls]
    for ls in (rows, cols)
]

galaxies = []
y = 0
for row, row_length in zip(rows, row_lengths):
    x = 0
    for char, col_length in zip(row, col_lengths):
        if char == '#':
            galaxies.append((x, y))
        x += col_length
    y += row_length

print(f"{len(galaxies)} galaxies")

answer = 0
for i, (x0, y0) in enumerate(galaxies):
    for (x1, y1) in galaxies[i+1:]:
        answer += abs(x1 - x0) + abs(y1 - y0)

print(f"Answer: {answer}")


# --- Compute answer in O(#galaxies) ---

xs, ys = zip(*galaxies)
xs = sorted(xs) # ys already sorted

total = 0
for cs in (xs, ys):
    dist = 0 # Sum of distances from galaxy i to previous galaxies
    for i in range(1, len(galaxies)):
        dist += i * (cs[i] - cs[i - 1])
        total += dist

print(f"Linear time answer: {total}")
