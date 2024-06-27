a,b = map(int,input().split())
c = []
sum = 0
for i in range(a):
    c.append(int(input()))
    sum = sum + c[i]

sub = b / sum
for i in range(a):
    print(int(c[i]*sub))
