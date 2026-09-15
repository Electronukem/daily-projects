# Task Dependency Batches (Hard)
# Group tasks into the minimum number of sequential batches such that every
# task in a batch can run in parallel (i.e. topological levels). Raises if
# the dependency graph has a cycle.
# Time: O(V + E) | Space: O(V + E)

from collections import defaultdict, deque

def batch_schedule(tasks, dependencies):
    graph = defaultdict(list)
    indegree = {t: 0 for t in tasks}
    for a, b in dependencies:
        graph[a].append(b)
        indegree[b] += 1

    batches = []
    current = deque(sorted(t for t in tasks if indegree[t] == 0))
    scheduled = 0
    while current:
        batch = sorted(current)
        batches.append(batch)
        scheduled += len(batch)
        next_wave = []
        for t in batch:
            for nxt in graph[t]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    next_wave.append(nxt)
        current = deque(next_wave)
    if scheduled != len(tasks):
        raise ValueError("Cycle detected in task dependencies")
    return batches

# Tests
assert batch_schedule(["a", "b", "c", "d"], [("a", "c"), ("b", "c"), ("c", "d")]) == [
    ["a", "b"], ["c"], ["d"]
]
try:
    batch_schedule(["x", "y"], [("x", "y"), ("y", "x")])
    assert False, "should have raised"
except ValueError:
    pass
print("All tests passed!")
