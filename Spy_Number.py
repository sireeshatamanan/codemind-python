a=int(input())
s=0
m=1
while a>0:
    n=a%10
    s+=n
    m*=n
    a=a//10
if s==m:
    print('Spy Number')
else:
    print('Not Spy Number')