n=int(input())
i=0
while 2**i<n:
    i+=1
if (2**i-n)>(n-2**(i-1)):
    print(n-2**(i-1))
else:
    print(2**i-n)