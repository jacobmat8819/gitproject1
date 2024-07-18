import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="88191988",
  database="jacobdb",auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()


#mycursor.execute("CREATE TABLE customers (name VARCHAR(255),address VARCHAR(255),city integer(10))")
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

#Insert values in to the table customers #

sql = "INSERT INTO customers (name, address,city) VALUES (%s, %s,%s)"
val = ("John", "Highway 21",771)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute("Select * from customers")

for y in mycursor:
    print(y)
