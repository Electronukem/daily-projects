# Knight's Tour via Warnsdorff's Heuristic (Hard)
# Find a path that visits every square of an n x n board exactly once using
# only knight moves, always stepping to the reachable square with the fewest
# onward options (breaking ties by position for determinism).
# Time: O(n^4) worst case | Space: O(n^2)

MOVES = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

def knights_tour(n, start=(0, 0)):
    visited = {start}
    path = [start]

    def degree(pos, visited):
        r, c = pos
        return sum(
            1 for dr, dc in MOVES
            if 0 <= r + dr < n and 0 <= c + dc < n and (r + dr, c + dc) not in visited
        )

    current = start
    while len(path) < n * n:
        r, c = current
        candidates = [
            (r + dr, c + dc) for dr, dc in MOVES
            if 0 <= r + dr < n and 0 <= c + dc < n and (r + dr, c + dc) not in visited
        ]
        if not candidates:
            return None
        candidates.sort(key=lambda pos: (degree(pos, visited), pos))
        current = candidates[0]
        visited.add(current)
        path.append(current)
    return path

# Tests
tour = knights_tour(5, (0, 0))
assert tour is not None
assert len(tour) == 25 and len(set(tour)) == 25
for (r1, c1), (r2, c2) in zip(tour, tour[1:]):
    assert (abs(r1 - r2), abs(c1 - c2)) in [(1, 2), (2, 1)]
print("All tests passed!")
