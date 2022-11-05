import math as m
def isprime(n):
    if n==1:
        return False
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            return False
            break
    return True
a=int(input())
s=0
for i in range(1,a):
    for j in range(1,a):
        if i*j==a:
            if isprime(i) and isprime(j):
                s=1
                print(i,j)
                break
        if s==1:
            break
if s==0:
    print(-1)