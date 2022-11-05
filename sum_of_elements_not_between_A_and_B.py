n=int(input())
v=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in v:
    if i<a or i>b:
        s+=i
print(s)