n=int(input())
v=list(map(int,input().split()))
i=0
for k in range(len(v)):
    if v[k]%2!=0:
        i=k
print(i)
