n=int(input())
v=list(map(int,input().split()))
c=int(input())
s=0
for k in range(len(v)):
    if v[k]==c:
        s+=1
print(s)