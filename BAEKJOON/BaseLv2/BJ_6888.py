a = int(input())
b = int(input())
c = 0
for i in range(a,b+1):
    if c==0:
        print("All positions change in year",a)
        c=c+1
        continue
    if c%60==0:
        print("All positions change in year",c+a)
    c=c+1