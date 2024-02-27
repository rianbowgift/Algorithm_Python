a = int(input())
for i in range(0,a):
    b,c,d,e = map(int,input().split())
    if c+d+e<55 or c<11 or d<8 or e<=12:
        print(b,c+d+e,"FAIL")
    else:
        print(b,c+d+e,"PASS")