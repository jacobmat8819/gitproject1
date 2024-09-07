import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="88191988",
  database="northwind",auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM Products")

for x in mycursor:
  print(x)





