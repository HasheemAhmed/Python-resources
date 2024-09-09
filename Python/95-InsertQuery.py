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

    sql = "INSERT INTO studentinfo VALUES (%s,%s)"
    val = (2,"Atif")
    cursor.execute(sql,val)

    # use to save the data
    mydb.commit()

    # use to get the row count
    print(f"{cursor.rowcount} rows inserted.")
except Error as e:
    print(f"Error : {e.msg} ")
    # print the error to screen if connection fails or databse is not created



# closing my db connection
if mydb:
    mydb.close()


