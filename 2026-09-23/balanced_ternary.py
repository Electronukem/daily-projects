# Balanced Ternary Conversion (Medium)
# Convert integers to and from balanced ternary, a base-3 system using
# digits {-1, 0, 1} (written as 'T', '0', '1') that needs no separate sign.
# Time: O(log n) | Space: O(log n)

def to_balanced_ternary(n):
    if n == 0:
        return "0"
    digits = []
    while n != 0:
        r = n % 3
        if r == 0:
            digits.append("0"); n //= 3
        elif r == 1:
            digits.append("1"); n //= 3
        else:
            digits.append("T"); n = (n + 1) // 3
    return "".join(reversed(digits))

def from_balanced_ternary(s):
    n = 0
    for ch in s:
        n = n * 3 + {"T": -1, "0": 0, "1": 1}[ch]
    return n

# Tests
assert to_balanced_ternary(5) == "1TT"
assert from_balanced_ternary("1TT") == 5
assert to_balanced_ternary(0) == "0"
for n in range(-40, 41):
    assert from_balanced_ternary(to_balanced_ternary(n)) == n
print("All tests passed!")
