import math
a=int(input())
b=int(input())
c=0
def prim(a):
    if a<=1: return 0
    for i in range(2,int(math.sqrt(a))+1):
        if a%i==0:
            return 0
    return 1
for i in range(a,b+1):
    if prim(i):
        c+=1
print(c)