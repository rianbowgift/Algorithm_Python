a = int(input())

for q in range(1,a+1):
    for i in range(a-q,0,-1):
        print(" ",end='')
    for i in range(a-q,a):
        print("*",end='')
    print("")