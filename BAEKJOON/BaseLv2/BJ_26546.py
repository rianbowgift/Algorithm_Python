a = int(input())
for i in range(a):
    b,c,d = map(str,input().split())
    print(b[0:int(c)],end='')
    print(b[int(d):])