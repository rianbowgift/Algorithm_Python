a,b = map(int,input().split())
for i in range(0,a):
    c = input()
    for j in range(b,0,-1):
        print(c[j-1],end='')
    print()
