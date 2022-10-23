a=int(input())
t=a
a=a*a
s=0
while a>0:
    m=a%10
    s+=m
    a=a//10
if s==t:
    print('Neon Number')
else:
    print('Not Neon Number')