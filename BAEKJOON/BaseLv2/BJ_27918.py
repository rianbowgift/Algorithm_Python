a = int(input())
d = 0
p = 0
for i in range(a):
    b = input()
    if b == 'D':
        d= d+1
    else :
        p = p+1
    if d-p==2 or p-d ==2:
        break
print(f'{d}:{p}')
