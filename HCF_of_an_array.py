n=int(input())
a=list(map(int,input().split()))
x=a[0]
i=1
while i<n:
    if a[i]%x==0:
        i+=1
    else:
        x=a[i]%x
print(x)