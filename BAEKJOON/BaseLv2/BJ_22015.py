a= list(map(int,input().split()))
b = sorted(a)
c = b[2]-b[0]
c = c + b[2]-b[1]
print(c)