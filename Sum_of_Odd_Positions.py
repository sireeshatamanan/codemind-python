_=int(input())
v=list(map(int,input().split()))
s=0
for k in range(len(v)):
    if k%2!=0:
        s+=v[k]
print(s)