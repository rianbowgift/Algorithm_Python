a = int(input())
sum = 0
for i in range(a):
    b = input()
    c = int(b[2:])
    if c <=90:
        sum = sum +1
print(sum)