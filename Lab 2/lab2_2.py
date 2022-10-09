m0 = int(input("Enter the dimensions of the matrices: "))
n0 = int(input())
dict0 = {}
dict1 = {}
print("First matrix values: ")
for i in range(m0*n0):
    val = int(input())
    if val!=0:
        dict0[i] = val
print("Second matrix values: ")
for i in range(m0*n0):
    val = int(input())
    if val!=0:
        dict1[i] = val
count = 0
for i in range(m0*n0):
    val = dict0.get(i)+dict1.get(i)
    if(count==n0-1):
        print(val)
        count = 0
    else:
        print(val, end = ' ')
        count = count + 1
