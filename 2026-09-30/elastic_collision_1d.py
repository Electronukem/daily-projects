# 1D Elastic Collision Resolver (Hard)
# Compute post-collision velocities for two masses colliding elastically on
# a line, and verify the result against the physical conservation laws it's
# derived from.
# Time: O(1) | Space: O(1)

def resolve_elastic_collision(m1, v1, m2, v2):
    total = m1 + m2
    new_v1 = ((m1 - m2) * v1 + 2 * m2 * v2) / total
    new_v2 = ((m2 - m1) * v2 + 2 * m1 * v1) / total
    return new_v1, new_v2

def momentum(m1, v1, m2, v2):
    return m1 * v1 + m2 * v2

def kinetic_energy(m1, v1, m2, v2):
    return 0.5 * m1 * v1 ** 2 + 0.5 * m2 * v2 ** 2

# Tests
m1, v1, m2, v2 = 2, 3, 5, -1
nv1, nv2 = resolve_elastic_collision(m1, v1, m2, v2)
assert abs(momentum(m1, nv1, m2, nv2) - momentum(m1, v1, m2, v2)) < 1e-9
assert abs(kinetic_energy(m1, nv1, m2, nv2) - kinetic_energy(m1, v1, m2, v2)) < 1e-9

# Equal masses simply exchange velocities
nv1, nv2 = resolve_elastic_collision(4, 10, 4, -2)
assert abs(nv1 - (-2)) < 1e-9 and abs(nv2 - 10) < 1e-9
print("All tests passed!")
