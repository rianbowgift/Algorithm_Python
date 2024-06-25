a,b,c = map(int,input().split())

if a*b >( c*b ) + a:
    print("2")
elif a*b < ( c*b ) + a:
    print("1")
else:
    print("0")