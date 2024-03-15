w=0
l=0
for i in range(0,6):
    a = input()
    if a=='W':
        w=w+1
    else:
        l=l+1

if w>=5:
    print("1")
elif w>=3:
    print("2")
elif w>=1:
    print("3")
else:
    print("-1")