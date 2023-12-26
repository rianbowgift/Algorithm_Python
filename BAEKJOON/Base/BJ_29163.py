a = int(input())
b = list(map(int,input().split()))
d=0
e=0
for i in range(a):
   if b[i]%2==0:
       d+=1
   else:
       e+=1

if d>e:
    print("Happy")
else:
    print("Sad")