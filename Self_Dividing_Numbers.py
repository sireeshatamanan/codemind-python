def div(a):
    t=a
    while a!=0:
        m=a%10
        if a%10==0 or t%m!=0:
            return 0
        a=a//10
    return 1
x=int(input())
y=int(input())
for i in range(x,y+1):
    if div(i):
        print(i,end=' ')
            
        