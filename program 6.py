'''l=list(map(int,input("enter numbers").split()))
print(l)
product=1
sum=0
for i in l:
    product=product*i
    
if product<750:
    print(product)
else:
    for j in l:
        sum=sum+j
    print(sum)
l=["ashok","raj(cse girls king)","santhosh"]
n=[]
for i in l:
    if "b" in i:
     n.append(i)
print(n)
s=set(map(int,input("enter numbers").split()))
print(s)
s={1,3,6}
s.update([5,6])
print(s)
s={1,2,3,4,5,6}
s.discard(4)
print(s)

s.discard(8)
s={1,2,3,4}
s1={1,2,3,4,5,6,7}
print(s1.issuperset(s))
                                                                                                                                                                                                                                                                                                                                       print(s.symmetric_difference(s1))
print(s)
print(s^s1)
t=(1,2,3,3,4)
print(t.count(2))'''
d={'name':'ashok','college':'pragati'}
print(d.pop('college'))
print(d)



                                                                                                                                                         


        
