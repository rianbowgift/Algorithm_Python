a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

f=0
g=0
if b%d==0:
    f=b//d
else:
    f=(b//d) +1

if c%e==0:
    g=c//e
else:
    g=(c//e) +1

print(a-max(f,g))