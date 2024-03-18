a= int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())

time=0
sw=0
while True:
    if a==b:
        print(time)
        break
    elif a<0:
        time=time+c
        a=a+1
        continue
    elif a==0 and sw==0:
        time=time+d
        sw=1
        continue
    elif sw==1 or a>0:
        time=time+e
        a=a+1
        continue
