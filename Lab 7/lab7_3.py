text = input("Enter file name: ")
for line in reversed(list(open(text))):
    print(line.rstrip())
