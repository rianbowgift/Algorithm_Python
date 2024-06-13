a,b,c = map(int,input().split())
sums = (a+b+c) // 3
move = (sums-a)*2
move = move + (sums-b)
print(move)