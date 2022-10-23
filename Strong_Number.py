a=int(input())
t=a
def fac(n):
    s=1
    while n>0:
        s*=n
        n=n-1
    return s
p=0
while a>0:
    m=a%10
    p+=fac(m)
    a=a//10
if t==p:
    print('The number %d is a strong number'%t)
else:
    print('The number %d is not a strong number'%t)