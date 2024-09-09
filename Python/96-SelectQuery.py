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

    # use to execure query
    cursor.execute("SELECT * FROM StudentInfo")

    # use to fetch the data
    result  = cursor.fetchall()

    # result stores and get as tuple
    for a,b in result:
        print(a,b)

except Error as e:
    print(f"Error : {e.msg} ")
    # print the error to screen if connection fails or databse is not created



# closing my db connection
if mydb:
    mydb.close()