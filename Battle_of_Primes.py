a=int(input())
b=int(input())
import math as m
def isprime(n):
    if n==1:
        return False
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            return False
            break
    return True
i=1
while 1:
    if isprime(a+b+i):
        print(i)
        break
    i+=1