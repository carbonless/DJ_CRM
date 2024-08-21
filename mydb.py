import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'NewPassword',

    )

#prepare a cursor

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE mynewdatabase")
print("All Done!") 