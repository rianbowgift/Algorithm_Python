a = int(input())
for i in range(a):
    b = input()
    if b[-1:] != '.':
        b = b + '.'
    print(b)
