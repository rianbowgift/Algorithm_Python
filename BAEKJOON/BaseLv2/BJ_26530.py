a = int(input().strip())
e = []

for _ in range(a):
    b = int(input().strip())
    d = 0.0
    for _ in range(b):
        c = input().strip().split()
        f = c[0]
        g = int(c[1])
        h = float(c[2])
        d += g * h
    e.append(f"{d:.2f}")

for i in e:
    print("$" + i)
