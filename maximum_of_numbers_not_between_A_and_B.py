n=int(input())
v=list(map(int,input().split()))
a,b=map(int,input().split())
if max(v)<a or max(v)>b:
    print(max(v))
else:
    print(-1)