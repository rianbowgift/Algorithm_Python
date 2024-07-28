a, b, c, d = map(int, input().split())

e = a * b
f = c * d

if e > f:
    print("M")
elif e < f:
    print("P")
else:
    print("E")