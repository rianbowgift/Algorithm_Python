a, b = map(int, input().split())

c = 0

if a >= 8:
    c = a - 7
else:
    c = b + 7

print(c)