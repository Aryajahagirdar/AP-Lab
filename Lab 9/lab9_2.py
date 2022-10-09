try:
    x = float(input("Enter number 1:"))
except:
    print("Error: Wrong Input Type!")
    exit()

try:
    y = float(input("Enter number 2:"))
except:
    print("Error: Wrong Input Type!")
    exit()

while True:
    print("\nMENU")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("\nEnter the Choice: "))

    if choice == 1:
        sum1 = x+y
        print("Addition of numbers:")
        print(sum1)

    elif choice == 2:
        sub = x-y

        if sub < 0:
            print("Error: First number is lesser than second for subtraction.")
        else:
            print("Subtraction of numbers:")
            print(x-y)

    elif choice == 3:
        mul = x*y
        print("Multiplication of numbers: ")
        print(x, "*", y, "=", x*y)

    elif choice == 4:
        try:
            ans = x/y
        except:
            print("Error: Division by zero!")
        else:
            print("Division of numbers:")
            print(ans)

    elif choice == 5:
        break
