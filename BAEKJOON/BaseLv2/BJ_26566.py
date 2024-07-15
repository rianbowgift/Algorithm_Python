import math

a = int(input())

for i in range(a):
    b,c = map(int, input().split())
    d,e = map(int, input().split())


    bc = b /c
    de = (math.pi * d * d) / e

    if de > bc:
     print("Whole pizza")
    else:
     print("Slice of pizza")
