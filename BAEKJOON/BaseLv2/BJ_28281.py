a,b = map(int,input().split())
min = float('inf') # 무한대
money = list(map(int,input().split()))

for i in range(len(money)-1):
    x = (money[i]*b) + (money[i+1] *b)
    if x < min:
        min = x

print(min)


