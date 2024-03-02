a = int(input())
b = 0
x = list(map(int, input().split()))
for i in x:
    if i==a:
        b=b+1
print(b)