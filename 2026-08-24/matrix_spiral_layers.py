# Matrix Spiral Layers (Medium)
# Return the matrix as a list of concentric clockwise rings, outer ring first.
# Time: O(rows * cols) | Space: O(rows * cols)

def spiral_layers(matrix):
    if not matrix or not matrix[0]:
        return []
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    layers = []
    while top <= bottom and left <= right:
        layer = [matrix[top][c] for c in range(left, right + 1)]
        layer += [matrix[r][right] for r in range(top + 1, bottom + 1)]
        if top != bottom:
            layer += [matrix[bottom][c] for c in range(right - 1, left - 1, -1)]
        if left != right:
            layer += [matrix[r][left] for r in range(bottom - 1, top, -1)]
        layers.append(layer)
        top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
    return layers

# Tests
assert spiral_layers([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 2, 3, 6, 9, 8, 7, 4], [5]]
assert spiral_layers([[1, 2, 3, 4]]) == [[1, 2, 3, 4]]
print("All tests passed!")
