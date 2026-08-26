# Bracket Depth Profile (Medium)
# For each character in a string, report the nesting depth of any bracket type
# it belongs to (non-bracket characters inherit the current depth). Raises on
# unbalanced input.
# Time: O(n) | Space: O(n)

def depth_profile(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    opens, closes = set(pairs.values()), set(pairs.keys())
    depth = 0
    stack = []
    profile = []
    for ch in s:
        if ch in opens:
            depth += 1
            stack.append(ch)
            profile.append(depth)
        elif ch in closes:
            if not stack or stack[-1] != pairs[ch]:
                raise ValueError(f"Unbalanced bracket at position {len(profile)}: {ch}")
            stack.pop()
            profile.append(depth)
            depth -= 1
        else:
            profile.append(depth)
    if stack:
        raise ValueError("Unbalanced brackets: unclosed " + stack[-1])
    return profile

# Tests
assert depth_profile("a(b[c]d)e") == [0, 1, 1, 2, 2, 2, 1, 1, 0]
try:
    depth_profile("(]")
    assert False, "should have raised"
except ValueError:
    pass
print("All tests passed!")
