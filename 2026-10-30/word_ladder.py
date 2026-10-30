# LeetCode 127 - Word Ladder (Hard)
# Find shortest transformation from beginWord to endWord changing 1 letter at a time.
# Time: O(M^2 * N) | Space: O(M^2 * N) where M=word length, N=word list size

from typing import List
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            word, depth = queue.popleft()
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word == endWord:
                        return depth + 1
                    if next_word in words and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, depth + 1))
        return 0

# Tests
sol = Solution()
assert sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
assert sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
print("All tests passed!")
