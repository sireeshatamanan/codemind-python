import math
for _ in range(int(input())):
    s=int(input())
    a=(s**0.5)
    if a==math.floor(a):
        print('True')
    else:
        print('False')