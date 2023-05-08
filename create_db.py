import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd= "Jlcm0907192001J",
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE mozarstore")

my_cursor.execute("SHOW DATABASE")
for db in my_cursor:
    print(db)