while True:
    a = input().split()
    if a[0] == "#":
        break
    a[1], a[2] = map(int, a[1:3])  # 첫 번째 요소를 제외하고 나머지 두 요소를 정수로 변환
    if a[1] > 17 or a[2] >= 80:
        print(a[0], "Senior")
    else:
        print(a[0], "Junior")