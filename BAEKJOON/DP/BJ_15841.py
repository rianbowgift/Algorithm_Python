while True:
    a = int(input())
    if a== -1:
        break
    b = [1] * (a+1)
    if a<3:
        print(f"Hour {a}: 1 cow(s) affected")
    else:
        b[0] = 1
        b[1] = 1
        b[2] = 1
        for i in range(3,a+1):
            b[i] =  b[i-1]+b[i-2]
        print(f"Hour {a}: {b[a]} cow(s) affected")