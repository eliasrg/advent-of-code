with open('input.in') as f:
    board = f.read().split('\n')

pipes = {
    '|': [(0, 1), (0, -1)],
    '-': [(1, 0), (-1, 0)],
    'L': [(1, 0), (0, -1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(-1, 0), (0, 1)],
    'F': [(1, 0), (0, 1)]
}

steps = 0
area = 0
def step(dx, dy):
    global x, y, steps, area
    steps += 1
    area += x * dy
    x += dx
    y += dy

# Find starting point
for y, row in enumerate(board):
    for x, pipe in enumerate(row):
        if pipe == 'S':
            x0, y0 = x, y

x, y = x0, y0

# First step
for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    if (-dx, -dy) in pipes[board[y + dy][x + dx]]:
        step(dx, dy)
        break

# Continue following the pipe
while (x, y) != (x0, y0):
    dx, dy = next(dpos for dpos in pipes[board[y][x]]
                  if dpos != (-dx, -dy))
    step(dx, dy)

print(f"Furthest distance: {(steps + 1) // 2}")
print(f"Enclosed tiles: {abs(area) - steps // 2 + 1}")
