a,b,c = map(int,input().split())

if a==b and b!=c:
    print("C")
elif b==c and b!=a:
    print("A")
elif c==a and b!=c:
    print("B")
else:
    print("*")