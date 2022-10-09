import random

dict = {}
while(1):
    num = input("Enter num: ")
    if num=='-1':
        break
    dict[random.randrange(0, 100)] = num
sum1 = 0
nums=0
str1 = ' '
for i in dict.values():
    try:
        sum1 = sum1 + int(i)
        nums = nums + 1
    except:
        str1 = str1 + i
avg = sum1/nums
print("Average = ", avg)
print("Concatenated string = ", str1)
val = input("Enter value: ")
print(val in dict.values())
specchar = "!@#$%^&*<>?"
for i in dict.values():
    if i in specchar:
        print(i)
        
    
    
