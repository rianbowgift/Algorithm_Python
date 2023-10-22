a = int(input())
b = input()
count=0

for i in b:
    if i in ['a','e','i','o','u']:
        count= count+1

print(count)