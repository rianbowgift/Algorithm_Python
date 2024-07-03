a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    print(b,c)
    if b>=2:
        print( ((c-2) * b) +2)
    else:
        print(c*b)
