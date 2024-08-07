a = int(input())


b = list(map(int,input().split()))
sum = 8*(a-1)
for i in range(len(b)):
    sum += b[i]

print((sum//24),sum%24)