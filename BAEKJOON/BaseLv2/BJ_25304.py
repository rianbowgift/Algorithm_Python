a = int(input())
count = int(input())
sum=0
for i in range(count):
    b,c = map(int,input().split())
    sum+= b*c
if sum==a:
    print("Yes")
else:
    print("No")
