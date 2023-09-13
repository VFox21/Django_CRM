#Okay okay

import mysql.connector

dataBase = mysql.connector.connect(

	host = 'localhost',
	user = 'root',
	passwd = 'admin'

	)

#prepare a cursor object

cursosObject = dataBase.cursor()

#Create a database

cursosObject.execute("CREATE DATABASE dcrm_db")

print("All Done!!")