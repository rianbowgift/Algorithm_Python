n,m = map(int,input().split())

a,b = [],[]


for i in range(n):
    rows = list(map(int,input().split()))
    a.append(rows)

for i in range(n):
    rows = list(map(int,input().split()))
    b.append(rows)

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j],end=' ')
    print()