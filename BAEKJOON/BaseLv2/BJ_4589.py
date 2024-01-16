a = int(input())
print("Gnomes:")
for i in range(0,a):
    b = list(map(int,input().split()))
    if b[0]<b[1]<b[2] or b[0]>b[1]>b[2]:
        print("Ordered")
    else:
        print("Unordered")