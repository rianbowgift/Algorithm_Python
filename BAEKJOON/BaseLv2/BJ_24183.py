a = 229
b = 324
c = 297
d = 420
e = 210
f = 297

g =  (a * b * 2) * 1e-6
h = (c * d * 2) * 1e-6
i = (e * f) * 1e-6

aa,bb,cc = map(int,input().split())

j = g * aa
k = h * bb
l = i * cc
m = j+k+l
print(f"{m:.6f}")