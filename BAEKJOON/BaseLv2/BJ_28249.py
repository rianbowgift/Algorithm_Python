a = {'Poblano' : 1500,'Mirasol' : 6000, 'Serrano' : 15500, 'Cayenne': 40000, 'Thai' : 75000, 'Habanero' : 125000}
b = int(input())
sum = 0
for i in range(b):
    c = input()
    sum =sum + a[c]
print(sum)