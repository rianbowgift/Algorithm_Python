a, b = map(int, input().split())

a = 100 - a
b = 100 - b
c = 100 - (a + b)
d = a * b
q, r = divmod(d, 100)
print(a, b, c, d, q, r)
final_c = c + q
final_d = r
print(final_c, final_d)
