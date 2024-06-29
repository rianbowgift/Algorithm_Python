a = int(input())
for i in range(a):
    b = list(map(int, input().split()))
    print(f"{b[0]} {b[1]} {b[2]}")

    c = sum(1 for b in b if b    >= 10) # b요소들을 가저오면서 만족하면 1을구하고 더함


    if c==0:
        print("zilch")
    elif c==1:
        print("double")
    elif c==2:
        print("double-double")
    elif c==3:
        print("triple-double")

    print("")