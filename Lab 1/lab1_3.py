n = int(input("Enter input: "))
count=0
odd=[]
for i in range(0, n):
    print("Enter string", i+1, ":")
    name = input()
    print(name)
    if len(name) >= 2 and name[0] == name[-1]:
        count += 1
    if len(name)%2==1:
        odd.append(name)
print('Count =', count)
print(odd)


