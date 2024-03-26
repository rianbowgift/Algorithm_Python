a,b,c = map(int,input().split(':'))
a2,b2,c2 = map(int,input().split(':'))
e= ((a*3600)+(b*60)+c)
f= ((a2*3600)+(b2*60)+c2)
if e<f:
    print(f-e)
else:
    print(f-e+3600*24)