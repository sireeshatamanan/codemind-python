n=int(input())
v=list(map(int,input().split()))
s=0
for k in range(len(v)):
    if v[k]%2==0:
        s=k
print(s)