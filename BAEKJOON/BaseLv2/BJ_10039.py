
sums =0

for i in range(0,5):
    a= int(input())
    if a<40:
        sums=sums+40
    else:
        sums=sums+a
print(sums//5)

