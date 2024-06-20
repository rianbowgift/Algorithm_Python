a = int(input())
min = 3000;
min2 = 3000;
for i in range(a):
    b,c = map(int, input().split())
    if c>=b:
        if c-b<min2:
            min=c
            mins = c-b


if min==3000:
    print("-1")
else:
    print(min)
