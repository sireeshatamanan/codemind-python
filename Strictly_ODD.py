n=int(input())
v=list(map(int,input().split()))
s=0
e=0
for k in range(len(v)):
    if v[k]%2!=0 and k%2!=0:
        s+=1
    if v[k]%2!=0:
        e+=1
if s==e:
    print('True')
else:
    print('False')