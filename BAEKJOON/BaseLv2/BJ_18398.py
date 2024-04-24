a = int(input())
for i in range(0,a):
    b = int(input())
    for j in range(0,b):
        c,d = map(int,input().split())
        print(c+d, c*d)