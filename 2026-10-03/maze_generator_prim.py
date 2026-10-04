# Maze Generation via Randomized Prim's Algorithm (Hard)
# Carve a perfect maze (exactly one path between any two cells) out of a
# grid by growing a random spanning tree from a seeded frontier.
# Time: O(rows * cols) | Space: O(rows * cols)

import random
from collections import deque

def generate_maze(rows, cols, seed=42):
    rng = random.Random(seed)
    visited = {(0, 0)}
    passages = set()
    frontier = []

    def add_frontier(cell):
        r, c = cell
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                frontier.append((cell, (nr, nc)))

    add_frontier((0, 0))
    while frontier:
        idx = rng.randrange(len(frontier))
        cell, neighbor = frontier.pop(idx)
        if neighbor in visited:
            continue
        visited.add(neighbor)
        passages.add(frozenset((cell, neighbor)))
        add_frontier(neighbor)
    return passages

def _is_connected(passages, rows, cols):
    adj = {}
    for edge in passages:
        a, b = tuple(edge)
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    seen = {(0, 0)}
    q = deque([(0, 0)])
    while q:
        cur = q.popleft()
        for nxt in adj.get(cur, []):
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return len(seen) == rows * cols

# Tests
maze = generate_maze(5, 5, seed=42)
assert len(maze) == 5 * 5 - 1   # a spanning tree has exactly (cells - 1) edges
assert _is_connected(maze, 5, 5)
print("All tests passed!")
