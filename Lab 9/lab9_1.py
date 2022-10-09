class BookStore:
  def __init__(self, author, title, price, publisher, stockposition):
    self.author = author
    self.title = title
    self.price = price
    self.publisher = publisher
    self.stockposition = stockposition

p1 = BookStore("John", "Book1", 400, "Publisher1", 5)
p2 = BookStore("Jack", "Book2", 250, "Publisher1", 1)
p3 = BookStore("Jill", "Book3", 350, "Publisher1", 2)
p4 = BookStore("James", "Book4", 450, "Publisher1", 0)
p5 = BookStore("Jim", "Book5", 300, "Publisher1", 3)

print("Enter book author: ")
bookauthor = input()
print("Enter book title: ")
booktitle = input()

l1 = [p1, p2, p3, p4, p5]

for i in l1:
    if i.author==bookauthor and i.title==booktitle:
        print("Enter quantity of books: ")
        quantity = int(input())
        if i.stockposition<quantity:
            print("Required copies not in stock.")
        else:
            bookprice = i.price*quantity
            print("Price of Books = ", bookprice)
        exit()

print("Book not in inventory.")          
