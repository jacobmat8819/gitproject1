import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="88191988",
  database="northwind",auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()


#mycursor.execute("SELECT * FROM Customers ORDER BY Country, CustomerName;")
#mycursor.execute("select * from  customers where CustomerID = 'Ind'")

sql = "INSERT INTO Customers (CustomerName, City, Country) values (%s,%s,%s)"
val = [#('Cardinal', 'Stavanger', 'Norway')]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

for y in mycursor:
    print(y)