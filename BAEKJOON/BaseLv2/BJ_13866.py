a = list(map(int,input().split()))
b = sorted(a)
c = a[0]+a[3]
d = a[1]+a[2]
print(abs(c-d))