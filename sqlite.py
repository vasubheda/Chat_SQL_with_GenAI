import sqlite3

## Connect to sqlite
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record, create table
cursor=connection.cursor()

## Create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Vishwas','Data Science','A','90')''')
cursor.execute('''Insert Into STUDENT values('Neel','Data Science','B','100')''')
cursor.execute('''Insert Into STUDENT values('Avinash','Data Science','A','86')''')
cursor.execute('''Insert Into STUDENT values('Nikul','DEVOPS','A','91')''')
cursor.execute('''Insert Into STUDENT values('Dipak','DEVOPS','A','95')''')

## Display all the records
print("The inserted records are: ")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes to the database
connection.commit()
connection.close()