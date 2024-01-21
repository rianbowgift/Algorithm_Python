try:
    while True:
        a = input()
        sum = ""
        for i in range(len(a)):
            if a[i]=='e':
                sum= sum+'i'
            elif a[i] == 'i':
                sum = sum+'e'
            elif a[i] == 'E':
                sum = sum + 'I'
            elif a[i] == 'I':
                sum = sum + 'E'
            else:
                sum = sum + a[i]
        print(sum)
except:
    pass