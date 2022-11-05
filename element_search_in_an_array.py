_=int(input())
v=list(map(int,input().split()))
s=int(input())
f=0
for k in v:
    if k==s:
        print('True')
        f=1
        break
if f==0:
    print('False')