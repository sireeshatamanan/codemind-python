_=int(input())
v=list(map(int,input().split()))
a,b=[],[]
for i in v:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
print(*a+b)