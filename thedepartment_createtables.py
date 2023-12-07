import sqlite3

conn =sqlite3.connect('thedepartment.db')
cursor = conn.cursor()

quit = False
#print('Open databse successfully')

#create_table_query = "CREATE TABLE EMPLOYEES"

# Create Tables
#cursor.execute(''' CREATE TABLE IF NOT EXISTS EMPLOYEES (id INTEGER PRIMARY KEY, name varchar, department_id INTEGER, is_rover BOOLEAN)''')
#cursor.execute(''' CREATE TABLE IF NOT EXISTS DIVISIONS (id INTEGER PRIMARY KEY, name varchar)''')
#cursor.execute(''' CREATE TABLE IF NOT EXISTS DEPARTMENTS (id INTEGER PRIMARY KEY, name varchar, head_id INTEGER)''')
#cursor.execute(''' CREATE TABLE IF NOT EXISTS DEPARTMENT_MEMBERS (id INTEGER PRIMARY KEY, employee_id INTEGER, department_id INTEGER)''')
#cursor.execute(''' CREATE TABLE IF NOT EXISTS EMPLOYEE_PROJECTS (id INTEGER PRIMARY KEY, employee_id INTEGER, project_id INTEGER)''')
#cursor.execute(''' CREATE TABLE IF NOT EXISTS PROJECTS (id INTEGER PRIMARY KEY, name varchar, description text)''')


# Insert Data on each table
while not quit :
    print ("The Department")
    while True:
        choosetable = input('Please choose a table to add entry: Type (e) for Employees, (d) for Departments, (v) to view entry and (q) to exit: ')
        if choosetable.lower() == "e":
            name = input("Name: ")
            dept_id = input("Dept ID: ")
            is_rover = input("True or False: ")
            cursor.execute('INSERT INTO EMPLOYEES (name, department_id, is_rover) VALUES (?, ?, ?)', (name, dept_id, is_rover))
            conn.commit()
            continue
        elif choosetable.lower() == "d":
            name = input("Department name: ")
            head_id = input("Head ID: ")
            cursor.execute('INSERT INTO DEPARTMENTS (name, head_id) VALUES (?, ?)', (name, head_id))
            conn.commit()
            continue

        elif choosetable.lower() == "v":
            whattoview = int(input("Choose (1) for Employee List or (2) for Department: "))
            if whattoview == 1:
                cursor.execute('SELECT * FROM EMPLOYEES')
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            elif whattoview == 2:
                cursor.execute('SELECT * FROM DEPARTMENTS')
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
        
        elif choosetable.lower() == "q":
            quit = True
            break


        else:
            print("Invalid Input")
            continue
            



#cursor.execute('INSERT INTO EMPLOYEES (name, department_id, is_rover) VALUES (?, ?, ?)', ('duvall', 2, False))
#cursor.execute('INSERT INTO DIVISIONS (name) VALUES (?)', ['div1'])
#cursor.execute('INSERT INTO DEPARTMENTS (name, head_id) VALUES (?, ?)', ('dept1', 1))
#cursor.execute('INSERT INTO DEPARTMENT_MEMBERS (employee_id, department_id) VALUES (?, ?)', (1, 1))
#cursor.execute('INSERT INTO EMPLOYEE_PROJECTS (employee_id, project_id) VALUES (?, ?)', (1, 1))
#cursor.execute('INSERT INTO PROJECTS (name, description) VALUES (?, ?)', ('project1', 'test project1'))








#conn.close
#conn.commit()
#    #conn.close()


#conn.commit()
#cursor.execute('SELECT * FROM EMPLOYEES')
#rows = cursor.fetchall()
#for row in rows:
#    print(row)
               
#cursor.execute('SELECT * FROM DIVISIONS')
#rows = cursor.fetchall()
#for row in rows:
#    print(row)
#conn.commit()