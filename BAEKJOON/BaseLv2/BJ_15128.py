a,b,c,d = map(int,input().split())
s = a/b * c/d / 2
if int(s) == s:
    print(1)
else:
    print(0)