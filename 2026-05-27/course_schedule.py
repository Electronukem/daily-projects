# LeetCode 207 - Course Schedule (Medium)
# Determine if you can finish all courses given prerequisites (cycle detection).
# Time: O(V + E) | Space: O(V + E)

from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return count == numCourses

# Tests
sol = Solution()
assert sol.canFinish(2, [[1, 0]]) == True
assert sol.canFinish(2, [[1, 0], [0, 1]]) == False
assert sol.canFinish(4, [[1,0],[2,1],[3,2]]) == True
print("All tests passed!")
