n=int(input())
for i in range(n):
    a=int(input())
    if a==int(str(a)[::-1]):
        print('True')
    else:
        print('False')