import sys

a = sys.stdin.readline().rstrip()

for i in range(0,int(a)):
    b,c = sys.stdin.readline().rstrip().split()
    print(int(b)+int(c))