_=int(input())
v=list(map(int,input().split()))
s=0
for k in range(1,len(v)-1):
    if v[k-1]%2==0 and v[k+1]%2!=0:
        s+=1
    elif v[k-1]%2!=0 and v[k+1]%2==0:
        s+=1
print(s)