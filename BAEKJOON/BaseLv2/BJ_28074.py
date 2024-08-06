a = input()

b = ['M','O','B','I','S']

for char in b:
    if char in a:
        # 첫 번째로 등장하는 해당 문자만 제거
        a = a.replace(char, '', 1)
    else:
        print("NO")
        break
else:
    print("YES")