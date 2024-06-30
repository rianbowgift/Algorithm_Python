a = int(input())
for i in range(a):
    b = list(map(int, input().split()))
    for c in b:
        print(c,end=' ')
    print("")
    if 17 in b and 18 in b:
        print("both")
    elif 17 in b:
        print("zack")
    elif 18 in b:
        print("mack")
    else:
        print("none")
    print("")
