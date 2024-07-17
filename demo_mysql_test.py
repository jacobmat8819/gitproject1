import mysql.connector
mydb = mysql.connector.connect(
    user='root', password='88191988',
    host='localhost', database='northwind',
    auth_plugin='mysql_native_password')

mycursor = mydb.cursor()

mycursor.execute("SELECT CustomerName, City, Country FROM Customers;")
myresult = mycursor.fetchall()

for r in myresult:
    print(r)