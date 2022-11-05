_=int(input())
v=list(map(int,input().split()))
o=0
e=0
for k in range(len(v)):
    if k%2!=0:
        o+=v[k]
    else:
        e+=v[k]
print(abs(o-e))