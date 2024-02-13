a = int(input())
for i in range(0,a):
    b,c = map(int,input().split())
    if b*c ==1:
        print("0")
    elif (b*c)%2==0:
        print(b*c//2)
    else:
        print(int((b*c/2)))