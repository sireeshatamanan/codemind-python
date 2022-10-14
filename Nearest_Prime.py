for i in range(int(input())):
    n=int(input())
    a=n
    while True:
        c=0
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                c=1
                break
        if c==0:
            break
        else:
            a=a+1
    b=n
    while True:
        c=0
        for i in range(2,int(b**0.5)+1):
            if b%i==0:
                c=1
                break
        if c==0:
            break
        else:
            b=b-1
    if(a-n>=n-b):
        print(b)
    else:
        print(a)