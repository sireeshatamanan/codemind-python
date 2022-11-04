n=int(input())
if n==0:
    print(0)
a=0
b=1
c=0
while c<n:
    a=b
    b=c
    c=a+b
if (c-n)>(n-b):
    print(b)
elif (c-n)==(n-b):
    print(b,c)
else:
    print(c)