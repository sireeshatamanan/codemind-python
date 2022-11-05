n=int(input())
v=list(map(int,input().split()))
if (sum(v)//n) in v:
    print('True')
else:
    print('False')