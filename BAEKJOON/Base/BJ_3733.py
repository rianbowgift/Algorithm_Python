while True:
    try:
        a,b = map(int,input().split())
    except:
        break
    else:
        print(b//(a+1))
