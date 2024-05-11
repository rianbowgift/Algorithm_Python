a,b,c = map(int,input().split())
d,e,f = map(int,input().split())

if d >= a and e >= b and f >= c:
    print("A")
elif e >= b and f >= c and d >= a / 2:
    print("B")
elif e >= b and f >= c:
    print("C")
elif f >= c/2 and e >= b / 2:
    print("D")
else:
    print("E")
