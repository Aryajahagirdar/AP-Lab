def my_function(list1):
    for i in list1:
        if list1.count(i)>1:
            x = list1.count(i)
            for j in range(0, x-1):
                list1.remove(i)
    
    print(list1)

thislist = [1,1,1,2,2,2,2,2,3,3,3,3,3,4,4]
my_function(thislist)
