n=int(input())
square=n*n
s=str(n)
x=str(square)
if x.endswith(s):
   print("Automorphic Number")
else:
   print("Not an Automorphic Number")