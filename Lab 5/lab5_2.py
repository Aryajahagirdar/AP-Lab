class Vehicle:
  def __init__(self, owner, identification, manufacturer):
    self.owner = owner
    self.identification = identification
    self.manufacturer = manufacturer

    def add(self):
        print(self.owner, self.identification, self.manufacturer)

class Passenger(Vehicle):
  def __init__(self, owner, identification, manufacturer, noofpassengers):
    super().__init__(owner, identification, manufacturer)
    self.passengers = noofpassengers
    
  def printname(self):
    print("Owner Name:", self.owner, "\nIdentification Nmber:", self.identification, "\nManufacturer:", self.manufacturer, "\nNo. of passengers:", self.passengers)

owner = input("Enter name of owner: ")
id1 = input("Enter identification number: ")
mfg = input("Enter name of manufacturer: ")
pasg = input("Enter number of passengers: ")

x = Passenger(owner, id1, mfg, pasg)
x.printname()
