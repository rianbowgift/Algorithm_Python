a,b,c = map(int,input().split())

if a+b+c<100:
    d = min(a,b,c)
    if a==d:
        print("Soongsil")
    elif b==d:
        print("Korea")
    else:
        print("Hanyang")

else:
    print("OK")
