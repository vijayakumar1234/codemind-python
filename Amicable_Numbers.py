n=int(input())
m=int(input())
fc=0
fc2=0
for i in range(1,n):
   if n%i==0:
      fc=fc+i
for i in range(1,m):
   if m%i==0:
      fc2=fc2+i
if fc2==n and fc==m:
   print("Amicable")
else:
   print("Not Amicable")
      
      