a,b = map(int,input().split())
c = int(input())
for i in range(c):
    d = int(input())
    sum=0
    if d>1000:
        sum= (a*1000) + (d-1000)*b
        print(d,sum)
    else:
        print(d,a*d)