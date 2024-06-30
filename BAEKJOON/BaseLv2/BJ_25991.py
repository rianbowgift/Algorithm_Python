n = int(input())
c = list(map(float, input().split()))
b = sum(dd ** 3 for dd in c)
r = b ** (1/3)

print(f"{r:.6f}")