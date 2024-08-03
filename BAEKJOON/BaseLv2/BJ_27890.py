a,b = map(int,input().split())

for i in range(b):
        if a % 2 == 0:
            a = int(a/2) ^ 6
        else:
            a = (2*a) ^ 6
print(a)