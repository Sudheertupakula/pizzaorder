import mysql.connector
from tutorial import  *
mydb==mysql.connector.connect(host="localhost",user="sudheer",password="yellowmessenger")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE pizzaorder")
mycursor.execute("CREATE TABLE customers (name VARCHAR(255),orderID VARCHAR(255))")
sql="INSERT INTO customers (name,orderID) VALUES(%s,%s)"
val=((tutorial.customer[lname]+tutorial.customer[fname]), tutorial.item)
mydb.commit()
