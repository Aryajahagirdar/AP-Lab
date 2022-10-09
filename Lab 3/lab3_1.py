def my_function(list1):
  ans = 1;
  for x in list1:
    ans = ans *x
  return ans

list2 = []
a = int(input("Enter list size: "))
for i in range(0, a):
    val = int(input())
    list2.append(val)
        

i = my_function(list2)
print(i)
