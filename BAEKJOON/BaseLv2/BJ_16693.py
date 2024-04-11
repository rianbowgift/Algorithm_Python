import math
a,b =map(int,input().split())
c,d =map(int,input().split())

if b/a < d/(c**2*math.pi):
    print("Slice of pizza")
else:
    print("Whole pizza")