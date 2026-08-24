# Knight Reachable Squares (Hard)
# Count the distinct squares a knight can reach on an n x n board within a
# given number of moves, starting from a fixed square.
# Time: O(moves * frontier size) | Space: O(n^2)

def knight_reachable(n, start, moves):
    deltas = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    visited = {start}
    frontier = [start]
    for _ in range(moves):
        next_frontier = []
        for r, c in frontier:
            for dr, dc in deltas:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    next_frontier.append((nr, nc))
        frontier = next_frontier
        if not frontier:
            break
    return len(visited)

# Tests
assert knight_reachable(8, (0, 0), 1) == 3
assert knight_reachable(8, (0, 0), 0) == 1
print("All tests passed!")
