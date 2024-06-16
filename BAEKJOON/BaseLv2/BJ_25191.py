a = int(input())
b,c = map(int, input().split())
sum=0
while a>0:
    if b>=2:
     sum= sum+1
     b = b-2
     a = a-1
    elif c>=1:
        sum = sum+1
        c = c-1
        a = a-1
    else:
        print(sum)
        break


if a==0:
    print(sum)