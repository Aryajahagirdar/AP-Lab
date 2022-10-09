import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
f1 = open("valid.txt", "w")
f2 = open("invalid.txt", "w")

def check(email):   
    if(re.search(regex,email)):
            f1.write(email) 
    else:
            f2.write(email)
            
if __name__ == '__main__' :
    myfile = open("emails.txt", "r")
    for line in myfile:
        check(line)
    f1.close()
    f2.close()
    
    f1 = open("valid.txt", "r")
    f2 = open("invalid.txt", "r")
    print("Valid emails: ")
    for x in f1:
      print(x);

    print("\nInvalid emails: ")
    for y in f2:
      print(y);
    f1.close()
    f2.close()
