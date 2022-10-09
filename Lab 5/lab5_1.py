class Employee:
  def __init__(self, id1, name, salary, dept):
    self.id1 = id1
    self.name = name
    self.salary = salary
    self.dept = dept

  def add(self):
    print("ID: ", self.id1, "Name: ", self.name,"Salary: ", self.salary,"Department: ", self.dept)


x = int(input("Enter number of employees: "))
l1 = []
for i in range(0 ,x):
    t1 = ()
    a = input("ID: ")
    b = input("Name: ")
    c = input("Salary: ")
    d = input("Department: ")
    t1 = (a,b,c,d)
    l1.append(t1)
    #e1 = Employee(a,b,c,d)
    #e1.add()


x = input("Enter Employee ID: ")
for i in range(0, len(l1)):
    if l1[i][0]==x:
        y = Employee(l1[i][0], l1[i][1], l1[i][2], l1[i][3])
        y.add()
    else:
        continue

