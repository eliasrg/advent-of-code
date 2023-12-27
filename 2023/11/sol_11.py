expansion = 1000000

with open('input') as f:
    rows = f.readlines()

ys = []
xs = []
for y, row in enumerate(rows):
    for x, char in enumerate(row):
        if char == '#':
            xs.append(x)
            ys.append(y)

xs.sort() # ys already sorted

total = 0
for cs in (xs, ys):
    dist_sum = 0 # Sum of distances from galaxy i to previous galaxies
    for i in range(1, len(cs)):
        dist_to_last = 0 if cs[i] == cs[i-1] else \
            expansion * (cs[i] - cs[i-1] - 1) + 1
        dist_sum += i * dist_to_last
        total += dist_sum

print(total)
