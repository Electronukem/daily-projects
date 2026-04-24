# Spiral pattern — 31x31
import math
size = 31
grid = [[' ']*size for _ in range(size)]
cx, cy = size//2, size//2
chars = "●○◐◑ "
for i in range(size * size):
    angle = i * 0.15
    r = i * 0.04
    x = int(cx + r * math.cos(angle))
    y = int(cy + r * math.sin(angle))
    if 0 <= x < size and 0 <= y < size:
        grid[y][x] = chars[i % len(chars)]
for row in grid:
    print(''.join(row))
