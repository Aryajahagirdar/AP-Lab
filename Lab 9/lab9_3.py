class Bank:
    def __init__(self, name, age, accountnumber, accounttype, balance):
        self.name = name
        self.age = age
        self.accountnumber = accountnumber
        self.accounttype = accounttype
        self.balance = balance

    def printdetails(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Account Number: ", self.accountnumber)
        print("Account Type: ", self.accounttype)
        print("Balance: ", self.balance)

class CheckAccount(Bank):
    def __init__(self, name, age, accountnumber, accounttype, balance):
        super().__init__(name, age, accountnumber, accounttype, balance)

    def check(self):
        if self.age>18 and len(str(self.accountnumber)==5) and (self.accountnumber=="Savings" or self.accounttype=="Current"):
            return True
        else: 
            return False

# create new account
# deposit money
# withdraw money
# print account details

p1 = Bank("John", "34", 33634, "Savings", 50000)
p2 = Bank("Jack", "28", 57542, "Savings", 10000)
p3 = Bank("Jill", "45", 25496, "Current", 20000)
p4 = Bank("James", "22", 68212, "Current", 40000)
p5 = Bank("Jim", "31", 76508, "Current", 30000)

l1 = [p1, p2, p3, p4, p5]

while True:
    print("\nMENU")
    print("1. Create new account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Print account details")
    print("5. Exit")
    choice = int(input("\nEnter the Choice: "))

    if choice == 1:
        print("Enter name:")
        name = input()
        print("Enter age:")
        age = int(input())
        print("Enter account number:")
        acc = int(input())
        print("Enter account type:")
        type = input()
        print("Enter balance amount:")
        bal = int(input())
        p = CheckAccount(name, age, acc, type, bal)
        if p==True:
            x = Bank(name, age, acc, type, bal)
            l1.append(x)
        else:
            print("Wrong details entered.")

    elif choice == 2:
        print("Enter account number: ")
        num = int(input())
        print("Enter amount to be deposited: ")
        amt = int(input())
        for i in l1:
            if i.accountnumber==num:
                i.balance = i.balance + amt
                i.printdetails()

    elif choice == 3:
        print("Enter account number: ")
        num = int(input())
        print("Enter amount to be withdrawn: ")
        amt = int(input())
        for i in l1:
            if i.accountnumber==num:
                i.balance = i.balance - amt
                i.printdetails()

    elif choice == 4:
        print("Enter account number: ")
        num = int(input())
        for i in l1:
            if i.accountnumber==num:
                i.printdetails()

    elif choice == 5:
        break
