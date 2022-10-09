import re
txt=dir(re)
#print(txt)
res=[]
for fun in txt:
   if fun.__contains__('find'):
       res.append(fun)
res=sorted(res)
print(res)

