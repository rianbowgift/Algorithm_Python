a = int(input())
for i in range(1,a+1):
    if i%7==0 and i%11==0:
        print("Cheers!")
    elif i%7==0:
        print("Hurra!")
    elif i%11==0:
        print("Super!")
    else:
        print(i)
