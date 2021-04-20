# import generator as gen
# import getInput
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

mydb = mysql.connector.connect(
  host=HOST,
  user=USER,
  password=PASSWORD
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Fitness.Exercise")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)