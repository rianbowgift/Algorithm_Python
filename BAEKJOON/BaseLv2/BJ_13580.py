a = list(map(int,input().split()))
b = sorted(a)
if b[0]==b[1] or b[1]== b[2]:
    print("S")
elif b[0]+b[1]==b[2]:
    print("S")
else:
    print("N")

