n=int(input())
i=0
c=0
for i in range(0,20):
    if i*(i+1)==n:
        c=1
        break
    i+=1
if c==1:
    print('YES')
else:
    print('NO')