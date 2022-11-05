n=int(input())
v=list(map(int,input().split()))
s=0
for i in v:
    s+=2**(n-1)*i
    n-=1
print(s)