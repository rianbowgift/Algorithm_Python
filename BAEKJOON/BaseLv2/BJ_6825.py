a = float(input())
b = float(input())

c =  a/(b*b)
if c>=25:
    print("Overweight")
elif c>=18.5:
    print("Normal weight")
else:
    print("Underweight")