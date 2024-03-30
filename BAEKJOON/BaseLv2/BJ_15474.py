a,b,c,d,e = map(int,input().split())

f = (a//b + ( 1 if a%b else 0)) * c
g = (a//d + ( 1 if a%d else 0)) * e

print(min(f,g))