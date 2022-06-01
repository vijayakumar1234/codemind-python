n=int(input())
is_negative=0
rev=0
if n<0:
   n=-n
   is_negative=1
while n>0:
 r=n%10
 rev=rev*10+r
 n=n//10
if is_negative==0:
   print(rev)
else:
   print(-rev)
