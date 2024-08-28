a = int(input())
b = [1] * (a + 2)
for i in range(3, a + 2):
    b[i] = b[i - 1] + b[i - 2]
print((b[a + 1] * 2) + (b[a] * 2))