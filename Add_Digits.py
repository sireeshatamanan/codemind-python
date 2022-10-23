a=int(input())
s=0
while a>0:
   m=a%10
   s+=m
   a=a//10
   if a==0 and s>9:
       a=s
       s=0
print(s)