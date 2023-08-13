sum = [i for i in range(1,31)]

for i in range(1,29):
    a = int(input())
    sum.remove(a)

print(min(sum))
print(max(sum))