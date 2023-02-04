def neon(n):
         s=n*n
         sum=0
         while s>0:
          sum=sum+(s%10)
          s=s//10
         if sum==n:
            print("neon")
         else:
             print("not neon")
n=int(input("enter a number"))    
neon(n)
