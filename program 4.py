'''n=int(input("enter number"))
if n==500:
    print("yes")
    
else:
    print("no")
n=int(input("enter number"))
if n>0:
    if n%2==0:
        print("even positive")
    else:
        print("odd positive")
else:
    if n%2==0:
        print("even negative")
    else:
        print("odd negative")
num1,num2=map(int,input("enter two numbers").split())
if num1>num2:
    print(num1," is big")
else:
    print(num2,"is big")
n=100.8
if isinstance(n,int):
    print("integer")
else:
    print("float")
n1,n2,n3=map(int,input("enter three numbers").split())
if n1>n2 and n1>n3:
    print(n1,"is big")
elif n2>n1 and n2>n3:
    print(n2,"is big")
else:
    print(n3,"is big")
n=int(input("enter a number"))
if n%11==0:
     print(n,"is divisible by 11")
else:
    print(n,"not divisible by 11")
n=int(input("enter a nuimber"))
if n%2==0 and n%5==0:
    print(n,"is divisible by both 2 and 5")
else:
    print(n,"is not divisible by both 2 and 5")
i=2
while i<=20:
    print(i)
    i=i+2
i=1
while i<=30:
    print(i)
    i=i+2
for i in range(1,11):
    print(i)
for i in range(1,11,2):
    print(i)
for i in range(2,10,2):
    print(i)
for i in range(10,1,-2):
    print(i)
import random
n=random.randrange(1,50)
guess=int(input("enter any number"))
while n!=guess:
     if n>guess:
        print("low")
        guess=int(input("enter any number"))
     elif n<guess:
        print("high")
        guess=int(input("enter any number"))
     else:
        break
print("correct guess")'''


    

    
