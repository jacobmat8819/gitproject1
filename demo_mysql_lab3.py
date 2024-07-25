import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="88191988",
  database="northwind",auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()


#mycursor.execute("CREATE TABLE customers (name VARCHAR(255),address VARCHAR(255),city integer(10))")
#mycursor.execute("SHOW TABLES")

#for x in mycursor:
  #print(x)

#Insert values in to the table customers #

#sql = "INSERT INTO customers (name, address,city) VALUES (%s, %s,%s)"
#"""
#val = [
  #('Peter', 'Lowstreet 4',20),
  #('Amy', 'Apple st 652',21),
  #('Hannah', 'Mountain 21',23),
  #('Michael', 'Valley 345',25),
  #('Sandy', 'Ocean blvd 2',35),
  #('Betty', 'Green Grass 1',67),
  #('Richard', 'Sky st 331',78),
  #('Susan', 'One way 98',98),
  #('Vicky', 'Yellow Garden 2',27),
  #('Ben', 'Park Lane 38',38),
  #('William', 'Central st 954',54),
  #('Chuck', 'Main Road 989',89),
  #('Viola', 'Sideway 1633',63)]"""

#mycursor.executemany(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM Customers ORDER BY Country DESC;")

for y in mycursor:
    print(y)
