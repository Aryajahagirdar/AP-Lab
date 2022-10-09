import sqlite3
conn = sqlite3.connect("file1.db")
print("Database connected  successfully!")

conn.execute("DROP TABLE COMPANY");
conn.execute("CREATE TABLE COMPANY(ID INT PRIMARY KEY, NAME TEXT, AGE INT, SALARY REAL)");
print("Table created successfully.");

conn.execute("INSERT INTO COMPANY(ID, NAME, AGE, SALARY) VALUES(34507, 'Jim', 19, 2500000)");
conn.execute("INSERT INTO COMPANY(ID, NAME, AGE, SALARY) VALUES(47328, 'John', 20, 1800000)");
conn.execute("INSERT INTO COMPANY(ID, NAME, AGE, SALARY) VALUES(15842, 'Jack', 19, 3000000)");
conn.execute("INSERT INTO COMPANY(ID, NAME, AGE, SALARY) VALUES(64257, 'Jason', 21, 2200000)");
conn.execute("INSERT INTO COMPANY(ID, NAME, AGE, SALARY) VALUES(84259, 'Jill', 21, 1500000)");
print("Values inserted in table.");

cursor = conn.execute("SELECT* FROM COMPANY")
for row in cursor:
    print("\nID:", row[0])
    print("Name:", row[1])
    print("Age:", row[2])
    print("Salary:", row[3])

conn.execute("UPDATE COMPANY SET SALARY=2000000 WHERE NAME = 'John'");
conn.commit
print("\n-----After update:-----")
cursor = conn.execute("SELECT* FROM COMPANY")
for row in cursor:
    print("\nID:", row[0])
    print("Name:", row[1])
    print("Age:", row[2])
    print("Salary:", row[3])

print("\nDeleting Jill.")
conn.execute("DELETE FROM COMPANY WHERE NAME = 'Jill'");
conn.commit
print("\n-----After delete:-----")
cursor = conn.execute("SELECT* FROM COMPANY")
for row in cursor:
    print("\nID:", row[0])
    print("Name:", row[1])
    print("Age:", row[2])
    print("Salary:", row[3])
