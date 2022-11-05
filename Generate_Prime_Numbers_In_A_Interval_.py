import math as m
a=int(input())
b=int(input())
def isprime(n):
    if n==1:
        return False
    for j in range(2,int(m.sqrt(n))+1):
        if n%j==0:
            return False
            break
    return True
for i in range(a,b+1):
    if isprime(i):
        print(i)