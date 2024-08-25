a = int(input())
b = input()
h = 0
z = 0
for i in b:
    if int(i)%2 == 0:
        z= z+1
    else:
        h= h+1

if z == h:
    print("-1")
elif z > h:
    print("0")
else:
    print("1")

