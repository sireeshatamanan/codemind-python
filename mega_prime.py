import math as mt
n=int(input())
t=n
def isprime(n):
    if n==1:
        return False
    for i in range(2,int(mt.sqrt(n))+1):
        if n%i==0:
            return False
            break
    return True
c=0
if isprime(n):
    while n>0:
        if isprime(n%10):
            c+=1
        n=n//10
if c==len(str(t)):
    print('Mega Prime')
else:
    print('Not Mega Prime')