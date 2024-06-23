a = int(input())
max = 0
for i in range(a):
    b,c,d = map(int,input().split())
    num = b * (c+d)
    if b == (c+d):
        num = num * 2
    if max<num:
        max = num

print(max)
