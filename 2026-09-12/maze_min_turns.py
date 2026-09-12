# Maze Minimum Turns (Hard)
# Find a path between two points in a grid maze (0=open, 1=wall) that
# minimizes the number of direction changes, using 0-1 BFS.
# Time: O(rows * cols) | Space: O(rows * cols)

from collections import deque

def min_turns(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dist = {}
    sr, sc = start
    dist[(sr, sc, -1)] = 0
    dq = deque([(sr, sc, -1)])
    while dq:
        r, c, d = dq.popleft()
        cur = dist[(r, c, d)]
        for ndi, (dr, dc) in enumerate(dirs):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                cost = 0 if ndi == d or d == -1 else 1
                nd = cur + cost
                key = (nr, nc, ndi)
                if key not in dist or nd < dist[key]:
                    dist[key] = nd
                    (dq.appendleft if cost == 0 else dq.append)((nr, nc, ndi))
    er, ec = end
    candidates = [dist[(er, ec, di)] for di in range(4) if (er, ec, di) in dist]
    return min(candidates) if candidates else -1

# Tests
assert min_turns([[0, 0, 0]], (0, 0), (0, 2)) == 0
assert min_turns([[0, 0], [0, 0]], (0, 0), (1, 1)) == 1
assert min_turns([[0, 1], [1, 0]], (0, 0), (1, 1)) == -1
print("All tests passed!")
