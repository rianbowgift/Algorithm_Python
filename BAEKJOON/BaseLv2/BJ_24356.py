a, b, c, d = map(int, input().split())

e = a * 60 + b
f = c * 60 + d

if f >= e:
    g = f - e
else:
    g = (24 * 60 - e) + f

h = g
i = h // 30

print(h, i)
