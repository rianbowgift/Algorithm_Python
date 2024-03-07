a= list(map(int,input().split()))
e,f,g = map(int,input().split())

x=0
for i in a:
    if i==e:
        print(x+1)
        break
    else:
        x=x+1
if x==4:
    print(0)

#