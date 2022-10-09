l1=[1,2,3,4,5,6]
l2=[7,8,9,10,11,12]

l3=[]
for i in l1:
    if i%2==1:
        l3.append(i)
for i in l2:
    if i%2==0:
        l3.append(i)
#l3.sort()
print(l3)
