a=int(input())
def rev(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
c=0
if a<0:
    c=1
    a*=-1
res=rev(a)
if c==1:
    print(res*-1)
else:
    print(res)