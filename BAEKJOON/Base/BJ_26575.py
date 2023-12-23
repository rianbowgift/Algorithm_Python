a = int(input())
for i in range(a):
    b,c,d = map(float,input().split())
    print('$%.2f' % (b*c*d) )