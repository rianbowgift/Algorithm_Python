a = int(input())
b = list(map(int,input().split()))
c = 0
for i in b:
    if a==i:
        c=c+1
print(c)
