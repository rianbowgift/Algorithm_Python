while True:
    a = int(input())
    if a==0:
        break
    for i in range(1,a+1):
        for j in range(0,i):
            print("*",end='')
        print()