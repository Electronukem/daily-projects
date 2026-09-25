# Ray-Circle Intersection (Medium)
# Cast a 2D ray and find the nearest point where it hits any circle in a
# scene, solving the quadratic intersection equation per circle.
# Time: O(number of circles) | Space: O(1)

import math

def ray_circle_intersection(origin, direction, circles):
    ox, oy = origin
    dx, dy = direction
    length = math.hypot(dx, dy)
    if length == 0:
        raise ValueError("direction must be non-zero")
    dx, dy = dx / length, dy / length

    best_t, best_point = None, None
    for cx, cy, r in circles:
        fx, fy = ox - cx, oy - cy
        b = 2 * (fx * dx + fy * dy)
        c = fx * fx + fy * fy - r * r
        disc = b * b - 4 * c
        if disc < 0:
            continue
        sqrt_disc = math.sqrt(disc)
        for t in ((-b - sqrt_disc) / 2, (-b + sqrt_disc) / 2):
            if t >= 0 and (best_t is None or t < best_t):
                best_t, best_point = t, (ox + dx * t, oy + dy * t)
    return best_point

# Tests
assert ray_circle_intersection((0, 0), (1, 0), [(5, 0, 1)]) == (4.0, 0.0)
assert ray_circle_intersection((0, 0), (1, 0), [(5, 5, 1)]) is None
assert ray_circle_intersection((0, 0), (1, 0), [(5, 0, 1), (3, 0, 0.5)]) == (2.5, 0.0)
print("All tests passed!")
