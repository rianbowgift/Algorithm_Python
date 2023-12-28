a = int(input())
for i in range(a):
    b = list(map(int, input().split()))
    print(b[0]*(b[2]-1)+b[1])