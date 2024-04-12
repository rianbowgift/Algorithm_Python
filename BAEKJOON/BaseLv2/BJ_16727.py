a,b = map(int,input().split())
c,d = map(int,input().split())
e = a+d
f = b+c
if e > f:
    print("Persepolis")
elif f > e:
    print("Esteghlal")
else:
    if d > b:
        print("Persepolis")
    elif b > d:
        print("Esteghlal")
    else:
        print("Penalty")