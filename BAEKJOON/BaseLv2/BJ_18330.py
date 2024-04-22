a = int(input())
b = int(input())
c=0
d=0
if b+60 > a:
    c=a
else:
    c=b
d = c*1500+(a-c)*3000

print(d)