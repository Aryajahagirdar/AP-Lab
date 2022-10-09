def my_function(list1):
    list2 = []
    for i in list1:
        if list1.count(i)>1:
            if i in list2:
                continue
            else:
                list2.append(i)
            
    
    print(list2)

thislist = [1,1,1,2,2,2,2,2,3,3,3,3,3,4,4]
my_function(thislist)
