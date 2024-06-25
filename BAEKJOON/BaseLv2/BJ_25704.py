a = int(input())
b = int(input())
c = [50000,50000,50000,50000]

if a>=5:
    c[0] = b -500
if a>=10:
    c[1] = b * 0.9
if a>=15:
    c[2] = b - 2000
if a>=20:
    c[3] = b * 0.75

if a<5:
    print(b)
else:
    if min(c)<0:
        print("0")
    else:
        print(int(min(c)))