# Diamond pattern generator — size 9
n = 9
ch = "◆"
for i in range(n):
    spaces = abs(n//2 - i)
    stars = n - 2 * spaces
    print(' ' * spaces + (ch + ' ') * stars)
print()
# Hollow variant
for i in range(n):
    spaces = abs(n//2 - i)
    stars = n - 2 * spaces
    if stars <= 1:
        print(' ' * spaces + ch)
    else:
        print(' ' * spaces + ch + ' ' * (2*stars - 3) + ch)
