# Polynomial Arithmetic (Hard)
# Represent polynomials as coefficient lists (index = power of x) and
# implement addition, multiplication, and evaluation via Horner's method.
# Time: O(n*m) for multiply | Space: O(n+m)

def poly_add(a, b):
    n = max(len(a), len(b))
    result = [0] * n
    for i, coeff in enumerate(a):
        result[i] += coeff
    for i, coeff in enumerate(b):
        result[i] += coeff
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result

def poly_multiply(a, b):
    if not a or not b:
        return [0]
    result = [0] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            result[i + j] += ca * cb
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result

def poly_eval(a, x):
    result = 0
    for coeff in reversed(a):
        result = result * x + coeff
    return result

# Tests
assert poly_multiply([1, 1], [-1, 1]) == [-1, 0, 1]      # (x+1)(x-1) = x^2-1
assert poly_add([1, 2, 3], [3, 2]) == [4, 4, 3]           # (3x^2+2x+1)+(2x+3)
assert poly_eval([1, 1], 5) == 6                          # (x+1) at x=5
assert poly_eval([-1, 0, 1], 3) == 8                      # (x^2-1) at x=3
print("All tests passed!")
