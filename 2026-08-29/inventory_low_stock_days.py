# Inventory Low-Stock Ranges (Medium)
# Given daily stock levels, return the inclusive day-index ranges during which
# stock stayed continuously below a threshold.
# Time: O(n) | Space: O(n)

def low_stock_ranges(stock_levels, threshold):
    ranges = []
    start = None
    for i, level in enumerate(stock_levels):
        if level < threshold:
            if start is None:
                start = i
        elif start is not None:
            ranges.append((start, i - 1))
            start = None
    if start is not None:
        ranges.append((start, len(stock_levels) - 1))
    return ranges

# Tests
assert low_stock_ranges([10, 5, 3, 8, 2, 1, 9], 6) == [(1, 2), (4, 5)]
assert low_stock_ranges([1, 1, 1], 5) == [(0, 2)]
assert low_stock_ranges([9, 9, 9], 5) == []
print("All tests passed!")
