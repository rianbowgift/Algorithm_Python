a = int(input())
for i in range(a):
    b,c,d = map(int, input().split())
    print(min(b,min(c,d)))

