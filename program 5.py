n=int(input("enter a number"))
s=n**2
sum=0
while s>0:
    sum=sum+(s%10)
    s=s//10
if sum==n:
    print("yes")
else:
    print("no")
    
