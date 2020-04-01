import mysql.connector

connection = mysql.connector.connect(host='localhost', database="myDB", user='root', password='your_ROOT_Password')

if connection.is_connected():
    print("Connected to mysql Database")

connection.close()