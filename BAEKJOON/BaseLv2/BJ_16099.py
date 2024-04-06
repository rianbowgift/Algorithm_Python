a = int(input())
for i in range(0,a):
    b,c,d,e = map(int,input().split())
    if b*c > d*e:
        print("TelecomParisTech")
    elif b*c < d*e:
        print("Eurecom")
    else:
        print("Tie")