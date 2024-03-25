a,b,c = map(int,input().split())
d,e,f = map(int,input().split())
s = 0
if d>a:
    s+=d-a
if e>b:
    s+=e-b
if f>c:
    s+=f-c
print(s)