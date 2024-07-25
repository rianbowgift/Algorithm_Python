
w = int(input())
l = int(input())
h = int(input())

a = min(w, l)
b = max(w, l)

if a >= 2 * h and b <= 2 * a:
    print("good")
else:
    print("bad")