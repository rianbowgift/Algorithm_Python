a = [
'Never gonna give you up',
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop'
]

b = int(input())
d=0
for i in range(b):
    c = input()
    if c not in a:
        print("Yes")
        d=1
        break

if d==0:
    print("No")