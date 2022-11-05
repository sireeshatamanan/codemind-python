n=int(input())
v=list(map(int,input().split()))
s=0
for i in v:
    if i<=(sum(v)//n):
        s+=1
print(s)