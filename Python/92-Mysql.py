# using mysql in the Python

# mysql module is used to handle with mysql databses
import mysql.connector

# creating a connection to the mysql database
myDataBase = mysql.connector.connect(host = "localhost", user = "root",password = "sheemo")

cursor = myDataBase.cursor()

# query to see all the databses in the server 
cursor.execute("SHOW DATABASES")

# printing databses name

for x in cursor:
    print(x)

# handling error using try-except
try:
    cursor.execute("CREATE DATABASE PythonDatabase")
except mysql.connector.Error as e:
    print(f"Error : {e}")

# Closing the cursor

if cursor:
    cursor.close()

# closing the database connection
if myDataBase:
    myDataBase.close()