field = int(input())

for i in range(1,field+1):
    a,b,c,d = map(int,input().split())
    if a*b > c*d:
        print("TelecomParisTech")
    elif a*b < c*d:
        print("Eurecom")
    else:
        print("Tie")