a, b = map(int, input().split())
C, d = map(int, input().split())

s1 = a * 3 + b
s2 = C * 3 + d

if s1 > s2:
    print(f"1 {s1 - s2}")
elif s2 > s1:
    print(f"2 {s2 - s1}")
else:
    print("NO SCORE")
