class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))
    
    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print("Enter number of elements: ")
x = int(input())
l1=[]
print("Enter elements: ")
for x in range(0, x):
    a = int(input())
    l1.append(a)
print(py_solution().sub_sets(l1))
