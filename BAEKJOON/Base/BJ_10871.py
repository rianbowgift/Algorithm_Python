a,b = map(int,input().split())
answer = list(map(int,input().split()))


for i in range(a):
    if answer[i] < b:
        print(answer[i], end=" ")