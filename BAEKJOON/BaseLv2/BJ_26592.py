a = int(input())
for i in range(a):
    b,c = map(float,input().split())
    d = (b * 2) / c
    print(f'The height of the triangle is {d:.2f} units')

