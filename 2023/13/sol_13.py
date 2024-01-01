with open('input.in') as f:
    patterns = [[list(line.strip()) for line in section.splitlines()]
                for section in f.read().split('\n\n')]

def mirror_rows(pattern):
    n_rows = len(pattern)
    return [i for i in range(1, n_rows)
            if all(pattern[i + j] == pattern[i - j - 1]
                   for j in range(0, min(n_rows - i, i)))]

def mirror_rows_cols(pattern):
    return (mirror_rows(pattern),
            mirror_rows(list(map(list, zip(*pattern)))))

def modifications(pattern):
    def swap(char):
        return {'.': '#', '#': '.'}[char]

    n_rows = len(pattern)
    n_cols = len(pattern[0])
    for i in range(n_rows):
        for j in range(n_cols):
            pattern[i][j] = swap(pattern[i][j])
            yield pattern
            pattern[i][j] = swap(pattern[i][j])

def answer(part2):
    ans = 0

    for i, pattern in enumerate(patterns):
        rs1, cs1 = mirror_rows_cols(pattern)

        if part2:
            rs, cs = next((rs, cs) for rs, cs in map(mirror_rows_cols,
                                                     modifications(pattern))
                          if (rs, cs) not in [([], []), (rs1, cs1)])
            rs = [r for r in rs if r not in rs1]
            cs = [c for c in cs if c not in cs1]
        else:
            rs, cs = rs1, cs1

        assert len(rs) + len(cs) == 1
        r = (rs + [0])[0]
        c = (cs + [0])[0]
        ans += 100 * r + c

    return ans

print(f"Part 1: {answer(False)}")
print(f"Part 2: {answer(True)}")
