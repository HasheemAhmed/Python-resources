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
except Error as e:
    print(f"Error : {e.msg} ")
    # print the error to screen if connection fails or databse is not created

# closing my db connection
if mydb:
    mydb.close()


