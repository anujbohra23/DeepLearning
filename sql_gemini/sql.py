import sqlite3

# conntect to sqlite3
connection = sqlite3.connect("student.db")

# creating cursor obj to insert record, create table

cursor = connection.cursor()
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

# inserting records
cursor.execute("""Insert Into STUDENT values('Anuj','Data Science','A',80)""")
cursor.execute("""Insert Into STUDENT values('Bohra','Data Science','B',100)""")
cursor.execute("""Insert Into STUDENT values('Tora','Data Science','A',86)""")
cursor.execute("""Insert Into STUDENT values('Mra','DEVOPS','A',50)""")
cursor.execute("""Insert Into STUDENT values('Dipesh','DEVOPS','A',35)""")

print("the inserted records are")

data = cursor.execute("""Select * from STUDENT""")
for row in data:
    print(row)

# closing connection after queries are executed
connection.commit()
connection.close()
