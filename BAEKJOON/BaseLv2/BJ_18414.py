a,b,c = map(int,input().split())
if b<a and a<c: #사이값
    print(a)
else:
    if a<=b:
        print(b)
    else:
        print(c)