a,b,c = map(int,input().split())
sum = 0
# while True:
#     if a>=b:
#         print(sum)
#         break
#     else:
#         a=a+c
#         sum+=1

d = b-a #22
sum = d//c
if d%c!=0:
    sum+=1

print(sum)