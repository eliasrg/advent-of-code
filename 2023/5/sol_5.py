with open('input.in') as f:
    paragraphs = f.read().split('\n\n')

seeds = list(map(int, paragraphs[0].split()[1:]))
maps = [
    [tuple(map(int, line.split()))
     for line in paragraph.strip().split('\n')[1:]]
    for paragraph in paragraphs[1:]
]

# --- Part 1 ---
part1_lowest = float('inf')
for s in seeds:
    for m in maps:
        for dest, src, length in m:
            if src <= s < src + length:
                s = dest + s - src
                break
    part1_lowest = min(part1_lowest, s)

print(f"Part 1: {part1_lowest}")

# --- Part 2 ---
def clean_intervals(intervals):
    """Remove empty intervals, sort intervals by start point and merge
    overlapping intervals."""
    intervals.sort()
    intervals = [I for I in intervals if I[1] > 0]
    i = 0
    while i < len(intervals) - 1:
        (s0, l0), (s1, l1) = intervals[i:i+2]
        assert s0 <= s1
        if s1 <= s0 + l0:
            del intervals[i+1]
            intervals[i] = (s0, max(s0 + l0, s1 + l1) - s0)
        else:
            i += 1

    return intervals

# Reachable intervals in current step
intervals = clean_intervals(list(zip(seeds[::2], seeds[1::2])))
for m in maps:
    m.sort(key=lambda entry: entry[1]) # Sort by src

    next_intervals = []
    for s, l in intervals:
        # Step from s to s + l
        i = s # First non-mapped position
        for dest, src, length in m:
            # Map interval to the left?
            if src + length <= s:
                continue

            # Map interval to the right?
            if src >= s + l:
                break

            # Gap in map?
            if src > i:
                next_intervals.append((i, src - i))
                i = src

            # Map intersection [i, end) -> [i - src + dest, end - src + dest)
            end = min(src + length, s + l)
            next_intervals.append((i - src + dest, end - i))
            i = end

        # Last unmapped part
        next_intervals.append((i, s + l - i))

    intervals = clean_intervals(next_intervals)

part2_lowest = intervals[0][0]
print(f"Part 2: {part2_lowest}")
