# Creating a new database named "Jacobdb" #

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="88191988",auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE jacobdb")


# Getting the Output of all Available databases in mysql #


import mysql.connector
mydb = mysql.connector.connect(
    user='root', password='88191988',
    host='localhost', database='northwind',
    auth_plugin='mysql_native_password')

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


