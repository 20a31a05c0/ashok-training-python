'''import random as r
a=[1,2,3,4,5]
print(r.choice(a))
print(r.random"())
print(r.randint(19,25))
print(r.choices(a,k=4))
print(r.uniform(30,40))
z=dir(r)
print(z)
import math
z=dir(math)
print(z)
import calendar
print(calendar.calendar(2023))
print(calendar.month(2023,5))
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2023,5))
import datetime
a=datetime.datetime.now()
print(a)
sv=a.strftime("%y")
fv=a.strftime("%Y")
print("year short version",sv)
print("year full version",fv)
def sample():
    print("ashok")
    print("kumar")
sample()
def multi():
    n1=int(input("enter number"))
    n2=int(input("enter number"))
    n3=int(input("enter number"))
    prod=n1*n2*n3
    return prod

res=multi()
print(res)
def multi(a,b,c):
    prod=a*b*c
    return prod
res=multi(2,3,4)
print(res)
def lemon():
    n=int(input("enter a number"))
    if n>21:
        print("exceed the lemons",n-21)
    elif n<21:
        print("insufficient lemons",21-n)
lemon()
def factor():
    l=[]
    n=int(input("enter a number"))
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    return l

res=factor()
print(res)
def multi(a):
    for i in range(1,13):
        b=str(a)+"*"+str(i)+'='+str(a*i)
        print(b)
n=int(input("enter a number"))
multi(n)
def sumofdigits(a):
    sum=0
    while a>0:
        sum=sum+(a%10)
        a=a//10
    return sum
n=int(input("enter a number"))
res=sumofdigits(n)
print(res)'''

