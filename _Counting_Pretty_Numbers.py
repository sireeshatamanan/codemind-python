for _ in range(int(input())):
    c=0
    a,b=map(int,input().split())
    for i in range(a,b+1):
        if i%10==2 or i%10==3 or i%10==9:
            c+=1
    print(c)
            