import math as m
n=int(input())
s=n*n
d=s%m.pow(10,len(str(n)))
if n==d:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')