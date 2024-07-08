a = int(input())

for f in range(a):
    a, b = map(float, input().split())
    an = abs(a - b)
    print(f"{an:.1f}")
