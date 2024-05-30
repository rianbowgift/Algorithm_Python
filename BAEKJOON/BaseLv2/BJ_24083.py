a = int(input())
b = int(input())
c = a+b
while True:
    if c>12:
        c=c-12
        continue
    else:
        if c==12:
            print("12")
        else:
            print(c)
        break