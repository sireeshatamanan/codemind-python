def ispal(n):
    if n==int(str(n)[::-1]):
        return True
    else:
        return False
a=int(input())
c=a+1
d=a-1
while 1:
    if ispal(c):
        break
    c+=1
while 1:
    if ispal(d):
        break
    d-=1
if c-a>a-d:
    print(d)
elif c-a<a-d:
    print(c)
else:
    print(d,c)