# Anagram Bucket Grouping (Medium)
# Group words into anagram buckets, ignoring case and non-letter characters.
# Time: O(n * k log k) | Space: O(n)

import re
from collections import defaultdict

def group_anagrams(words):
    buckets = defaultdict(list)
    for w in words:
        cleaned = re.sub(r"[^a-zA-Z]", "", w).lower()
        key = "".join(sorted(cleaned))
        buckets[key].append(w)
    return [sorted(buckets[key]) for key in sorted(buckets)]

# Tests
assert group_anagrams(["listen", "silent", "Enlist", "banana", "Ananab", "cat"]) == [
    ["Ananab", "banana"], ["cat"], ["Enlist", "listen", "silent"]
]
assert group_anagrams(["abc", "bca", "xyz"]) == [["abc", "bca"], ["xyz"]]
print("All tests passed!")
