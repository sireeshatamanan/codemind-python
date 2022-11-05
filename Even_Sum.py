_=int(input())
v=list(map(int,input().split()))
s=0
for k in v:
    if k%2==0:
        s+=k
print(s)