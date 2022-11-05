_=int(input())
v=list(map(int,input().split()))
s=0
e=0
for k in v:
    if k%2!=0:
        s+=k
    else:
        e+=k
print(abs(s-e))