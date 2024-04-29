a = int(input())
for i in range(0,a):
    b = input()
    c = len(b[:b.index("D")]) if "D" in b else len(b)
    print(c)