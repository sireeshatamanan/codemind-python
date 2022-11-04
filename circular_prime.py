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
if isprime(a) and isprime(int(str(a)[::-1])):
    print('circular prime')
elif isprime(a) and not(isprime(int(str(a)[::-1]))):
    print('prime but not a circular prime')
else:
    print('not prime')