a = list(map(int,input().split()))


c = (a[0]-11)*60*24 + (a[1]-11)*60 + (a[2]-11)
print(c if c >= 0 else -1)