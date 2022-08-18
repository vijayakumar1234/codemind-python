n=int(input())
fc_sum=0
for i in range(1,n):
    if n%i==0:
        fc_sum+=i
if fc_sum==n:
    print("True")
else:
    print("False")