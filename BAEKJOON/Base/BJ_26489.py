sum=0
while True:
    try:
        a = input()
        sum+=1
    except EOFError:
        break
print(sum)