a = int(input())
sum=0
for i in range(a):
    b = int(input())
    if b==1:
        sum+=1
    elif b==-1:
        sum-=1

if sum==0:
    print("Stay")
elif sum>0:
    print("Right")
else:
    print("Left")
