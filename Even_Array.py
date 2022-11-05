n=int(input())
v=list(map(int,input().split()))
s=0
for i in v:
    if i%2!=0:
        print('False')
        s=1
        break
if s==0:
    print('True')