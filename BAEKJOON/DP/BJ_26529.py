a = int(input())
b = [1] * 46
for i in range(2,46):
    b[i] = b[i-1] +b[i-2]

for i in range(a):
    c = int(input())
    print(b[c])