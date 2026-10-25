# Langton's Ant (Hard)
# Simulate an ant on an infinite grid: on a white cell, turn right, flip it
# black, and move; on a black cell, turn left, flip it white, and move.
# Simple local rules that produce emergent, non-trivial behavior.
# Time: O(steps) | Space: O(steps)

def simulate_ant(steps):
    x, y = 0, 0
    dx, dy = 0, 1  # facing north
    black = set()
    for _ in range(steps):
        pos = (x, y)
        if pos in black:
            dx, dy = -dy, dx       # turn left
            black.discard(pos)
        else:
            dx, dy = dy, -dx       # turn right
            black.add(pos)
        x, y = x + dx, y + dy
    return (x, y), (dx, dy), black

# Tests
pos, direction, black = simulate_ant(5)
assert pos == (-1, 0)
assert direction == (-1, 0)
assert black == {(1, 0), (1, -1), (0, -1)}

pos0, direction0, black0 = simulate_ant(0)
assert pos0 == (0, 0) and direction0 == (0, 1) and black0 == set()
print("All tests passed!")
