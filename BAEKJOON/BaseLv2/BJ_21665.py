n, m = map(int, input().split())
original = [input().strip() for _ in range(n)]
input()
negative = [input().strip() for _ in range(n)]

errors = 0
for i in range(len(original)):
    for j in range(len(original[i])):
        if original[i][j] == 'B' and negative[i][j] != 'W':
            errors += 1
        elif original[i][j] == 'W' and negative[i][j] != 'B':
            errors += 1
print(errors)