a = list(map(int,input().split()))

if a[0]*a[1]<=a[2]:
    print("0")
else:
    print((a[0]*a[1])-a[2])