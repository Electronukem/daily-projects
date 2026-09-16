# Word Frequency Ranking (Medium)
# Return the top-k most frequent words in a text, tie-broken alphabetically.
# Time: O(n log n) | Space: O(n)

import re
from collections import Counter

def top_k_words(text, k):
    words = re.findall(r"[a-zA-Z']+", text.lower())
    counts = Counter(words)
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return ranked[:k]

# Tests
text = "The quick brown fox. The FOX jumps over the lazy dog. Dog barks."
assert top_k_words(text, 5) == [("the", 3), ("dog", 2), ("fox", 2), ("barks", 1), ("brown", 1)]
print("All tests passed!")
