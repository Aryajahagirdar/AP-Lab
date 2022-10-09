import sqlite3
conn = sqlite3.connect("file.db")

#conn.execute("DROP TABLE student")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS student(id INT PRIMARY KEY, Name text, DOB text, Gender text, Course text)")
print("Table created successfully.")

conn.execute(
    "insert into student(id, Name, DOB, Gender, Course) values(34507, 'Jim', '29-02-2003', 'M', 'CCE')")
conn.execute(
    "insert into student(id, Name, DOB, Gender, Course) values(43728, 'Jill', '13-05-2002', 'F', 'CSE')")
conn.execute(
    "insert into student(id, Name, DOB, Gender, Course) values(15842, 'John', '24-11-2003', 'M', 'CCE')")
conn.execute(
    "insert into student(id, Name, DOB, Gender, Course) values(84259, 'Jenny', '08-06-2002', 'F', 'DSE')")
conn.execute(
    "insert into student(id, Name, DOB, Gender, Course) values(64257, 'Jack', '01-10-2002', 'M', 'CSE')")

print("Values inserted in table.")

while True:
    print("\n1. Add record.")
    print("2. Update record.")
    print("3. Delete record.")
    print("4. Show all records.")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        print("Adding new record -\n ")
        id1 = int(input("Enter student ID: "))
        name1 = input("Enter name: ")
        dob = input("Enter DOB: ")
        gender = input("Gender: ")
        courses = input("Student course: ")
        sql1 = "insert into student(id, Name, DOB, Gender, Course) values(?, ?, ?, ?, ?)"
        par = (id1, name1, dob, gender, courses)
        conn.execute(sql1, par)
        print("New Record Added.")

    elif ch == 2:
        print("Updating Record - \n")
        place=input("Enter field to be updated:\n")
        place=place+"="
        val = input("Enter field value:\n")
        val="'"+val+"'"
        id=input("Enter student ID:\n")
        id="'"+id+"'"
        updateQuery=" UPDATE STUDENT SET "+" "+place+ val +" "+ "WHERE ID="+ id
        conn.execute(updateQuery)
        print("Record updated successfully.")

    elif ch == 3:
        print("Deleting Record - ")
        print("Enter student id to be deleted: ")
        id1 = int(input())
        sql = "DELETE from student where id='{}'".format(id1)
        conn.execute(sql)
        print("Record deleted.\n")

    elif ch == 4:
        cursor = conn.execute("SELECT* FROM student")

        for row in cursor:
            print("\nID:", row[0])
            print("Name:", row[1])
            print("DOB:", row[2])
            print("Gender:", row[3])
            print("Course:", row[4])

    elif ch == 5:
        break
