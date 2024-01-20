a = int(input())


for i in range(0,a):
    back = ""
    c = ""
    b = input()
    for j in range(len(b)):
        if back==b[j]:
            back = b[j]
            continue
        else:
            c = c+b[j]
            back = b[j]

    print(c)

