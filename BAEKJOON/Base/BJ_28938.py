a = int(input())
b = list(map(int,input().split()))
c = 0
for i in range(a):
    if b[i]==1:
        c+=1
    elif b[i]==-1:
        c-=1

if c==0:
    print("Stay")
elif c>0:
    print("Right")
else:
    print("Left")
