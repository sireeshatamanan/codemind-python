import math as m
def isprime(n):
    if n==1:
        return False
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            return False
            break
    return True
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0 and not(isprime(i)):
        c+=1
print(c)