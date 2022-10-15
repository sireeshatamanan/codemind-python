a=int(input())
while True:
    a=int(str(a))+int(str(a)[::-1])
    if a==int(str(a)[::-1]):
        break
print(a)