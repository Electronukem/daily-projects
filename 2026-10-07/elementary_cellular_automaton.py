# Elementary Cellular Automaton (Medium)
# Simulate a Wolfram-style 1D cellular automaton: given an 8-bit rule number,
# an initial row, and a step count, generate each subsequent generation from
# its 3-cell neighborhood (fixed 0 boundary).
# Time: O(steps * width) | Space: O(steps * width)

def run_ca(rule, initial, steps):
    rule_bits = [(rule >> i) & 1 for i in range(8)]
    row = list(initial)
    history = [row[:]]
    for _ in range(steps):
        n = len(row)
        new_row = []
        for i in range(n):
            left = row[i - 1] if i > 0 else 0
            center = row[i]
            right = row[i + 1] if i < n - 1 else 0
            idx = (left << 2) | (center << 1) | right
            new_row.append(rule_bits[idx])
        row = new_row
        history.append(row[:])
    return history

# Tests
history = run_ca(30, [0, 0, 0, 1, 0, 0, 0], 1)
assert history == [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0]]
history2 = run_ca(90, [0, 0, 0, 1, 0, 0, 0], 1)  # Rule 90 = XOR of neighbors
assert history2[1] == [0, 0, 1, 0, 1, 0, 0]
print("All tests passed!")
