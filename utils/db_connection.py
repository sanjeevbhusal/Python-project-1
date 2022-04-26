import mysql.connector
db = mysql.connector.connect(
    host="localhost", user="root", passwd="1234", database="python_intern_1")
mycursor = db.cursor()
