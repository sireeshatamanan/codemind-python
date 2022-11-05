import math as m
def isprime(n):
    if n==1:
        return False
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            return False
            break
    return True
def ispal(n):
    if n==int(str(n)[::-1]):
        return True
    else:
        return False
n=int(input())
while 1:
    n+=1
    if isprime(n) and ispal(n):
        print(n)
        break