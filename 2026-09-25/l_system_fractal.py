# Lindenmayer System Expansion (Medium)
# Expand an L-system (axiom + per-character production rules) for a number
# of generations, as used to describe fractal plant growth and curves.
# Time: O(output length) | Space: O(output length)

def expand_l_system(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        current = "".join(rules.get(ch, ch) for ch in current)
    return current

# Tests
algae_rules = {"A": "AB", "B": "A"}
assert expand_l_system("A", algae_rules, 0) == "A"
assert expand_l_system("A", algae_rules, 1) == "AB"
assert expand_l_system("A", algae_rules, 4) == "ABAABABA"
assert [len(expand_l_system("A", algae_rules, i)) for i in range(6)] == [1, 2, 3, 5, 8, 13]
print("All tests passed!")
