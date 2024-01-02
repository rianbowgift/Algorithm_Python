a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    b =0
    c = input()
    if c=="#":
        break
    else:
        for pos in c:
            if pos in a:
                b= b+1
        print(b)