'''a=100
b=0
try:
    print(a/b)
except Exception as e:
    print("please note number ",e)
print("bye")
a=100
b=0
try:
    print(a/b)
except Exception as e:
    print("please note number ",e)
finally:
   print("bye")
a=10
try:
    b=int(input("enter a number"))
    print("resource is open")
    print(a/b)
except ZeroDivisionError as e:
    print("zero cant be divided",e)
except ValueError as e:
    print("invalid input",e) 
except Exception as e:
    print("other error",e)
finally:
    print("resource closed")
x=100
if x%2!=0:
    raise Exception("x should be even")
else:
    print(" x is even .. correct")
class computer:
    def config(self):
        print("yes")
lenova=computer()
lenova.config()'''
class computer:
    a=10
    b=20
    print("class variable inside",a)
    def config(self):
        c=100
        print("yes")
        print(self.a)
obj1=computer()
print(obj1.a)
obj1.config()
    


