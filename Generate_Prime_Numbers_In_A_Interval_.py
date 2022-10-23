import math
a=int(input())
b=int(input())
for i in range(a,b+1):
    c=0
    if i==1:
        c=1
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            c=1
    if c==0:
        print(i)