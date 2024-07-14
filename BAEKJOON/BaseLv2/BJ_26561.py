a = int(input())
for i in range(a):
    b,c = map(int, input().split())
    sum = b
    sum =sum + c//4 - c//7
    print(sum)
