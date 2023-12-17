a = int(input())

b = '7' in str(a)
c = a % 7 == 0

if b and c:
    print(3)
elif b:
    print(2)
elif c:
    print(1)
else:
    print(0)