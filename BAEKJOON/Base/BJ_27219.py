a = int(input())
b =""
while a!=0:
    if a>=5:
        b+="V"
        a-=5
    elif a>=1:
        b+="I"
        a-=1
print(b)