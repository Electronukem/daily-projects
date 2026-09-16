# Circular Stats Buffer (Medium)
# A fixed-size buffer that tracks the running average and maximum of the last
# N pushed values, both in O(1) amortized per push.
# Time: O(1) amortized per push | Space: O(N)

from collections import deque

class CircularStatsBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = deque()
        self.max_deque = deque()
        self.sum = 0

    def push(self, value):
        self.buffer.append(value)
        self.sum += value
        if len(self.buffer) > self.size:
            removed = self.buffer.popleft()
            self.sum -= removed
            if self.max_deque and self.max_deque[0] == removed:
                self.max_deque.popleft()
        while self.max_deque and self.max_deque[-1] < value:
            self.max_deque.pop()
        self.max_deque.append(value)

    def average(self):
        return self.sum / len(self.buffer) if self.buffer else 0

    def maximum(self):
        return self.max_deque[0] if self.max_deque else None

# Tests
buf = CircularStatsBuffer(3)
for v in [4, 2, 7, 1, 7, 3]:
    buf.push(v)
assert buf.maximum() == 7
assert abs(buf.average() - (1 + 7 + 3) / 3) < 1e-9

b2 = CircularStatsBuffer(2)
b2.push(5); b2.push(3)
assert b2.maximum() == 5 and b2.average() == 4
b2.push(1)
assert b2.maximum() == 3 and b2.average() == 2
print("All tests passed!")
