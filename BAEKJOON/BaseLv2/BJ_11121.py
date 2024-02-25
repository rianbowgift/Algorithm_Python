a = int(input())
for i in range(0,a):
    b,c = map(int,input().split())
    if b==c:
        print("OK")
    else:
        print("ERROR")