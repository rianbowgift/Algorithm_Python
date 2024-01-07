a = list(map(int,input().split()))
b = int(input())

a[2]= a[2]+b

while True:
    if a[2]>=60:
        a[1]= a[1]+1
        a[2]= a[2]-60
    else:
        break
while True:
    if a[1]>=60:
        a[0]= a[0]+1
        a[1]= a[1]-60
    else:
        break
while True:
    if a[0]>=24:
        a[0]= a[0]-24
    else:
        break

print(a[0],a[1],a[2])