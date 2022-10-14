for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    while(k):
        s=s[k-1::-1]+s[k:]
        k-=1
    print(s)