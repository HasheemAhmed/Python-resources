import mysql.connector
from mysql.connector import Error

# through this we can create databases and connect to it

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "sheemo",
        database = "PythonDatabase"
    )

    cursor = mydb.cursor()

    cursor.execute("CREATE TABLE StudentInfo(id INT PRIMARY KEY, sname VARCHAR(20) )") 

    cursor.execute("SHOW TABLES")

    for x in cursor:
        print(x)
except Error as e:
    print(f"Error : {e.msg} ")
    # print the error to screen if connection fails or databse is not created



# closing my db connection
if mydb:
    mydb.close()


