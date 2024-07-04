a = int(input())
for i in range(a):
    b,c,d = map(int,input().split())
    print("Data set:",b,c,d)
    for j in range(0,d):
        if b>c:
            b = b // 2
        else:
            c = c // 2
    if b>c:
        print(b,c)
    else:
        print(c,b)
    print("")