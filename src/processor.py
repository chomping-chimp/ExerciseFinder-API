import generator as gen
import getInput
import mysql.connector

mydb = mysql.connector.connect(
  host="sql3.freesqldatabase.com",
  user="sql3406581",
  password="K1FQBr2Tr1"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM sql3406581.Exercises")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)