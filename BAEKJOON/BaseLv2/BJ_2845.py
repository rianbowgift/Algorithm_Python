a = list(map(int,input().split()))
b = list(map(int,input().split()))

sum = a[0]*a[1]
for i in b:
    print(i-sum,end=' ')