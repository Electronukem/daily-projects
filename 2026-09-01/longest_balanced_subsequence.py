# Longest Balanced Subsequence (Hard)
# Find the longest subsequence (not necessarily contiguous) of parentheses
# that forms a balanced sequence, and return it alongside its length.
# Time: O(n) | Space: O(n)

def longest_balanced_subsequence(s):
    stack = []
    matched = set()
    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)
        elif ch == ")" and stack:
            open_i = stack.pop()
            matched.add(open_i)
            matched.add(i)
    result = "".join(s[i] for i in sorted(matched))
    return len(result), result

# Tests
assert longest_balanced_subsequence("()(()") == (4, "()()")
assert longest_balanced_subsequence("(())") == (4, "(())")
assert longest_balanced_subsequence(")))(((") == (0, "")
print("All tests passed!")
