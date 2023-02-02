#get onew string as input along with a character find out and display whether the particular character is present or not?
#palindrome?
#sting contains space or not if yes count no.of spaces and print?
'''n=input("enter string")
m=input("one character")
if m in n:
     print("yes")
else:
   print("no")
n=input("enter string")
q=n[ : :-1]
if q==n:
    print("palindrome")
else:
    print("not a palindrome")'''
m=input("enter a string")
n=' '
p=0
for i in m:
    if i==n:
        p=p+1
if p!=0:
    print(p)
else:
    print("no spaces")
