a = []
for i in range(0,6):
    a.append(int(input()))

b = sorted(a[:4])
c = sorted(a[4:])
print(b[2]+b[3]+b[1]+c[1])
