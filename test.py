import mysql.connector
import requests
import json
import paramiko


cnx = mysql.connector.connect(
  host='bs4ttoxa3uefryx7uje7-mysql.services.clever-cloud.com',
  user='ujypevobdznoejre',
  password='0f8Z8R1fpniQ0GkOxeYK',
  database='bs4ttoxa3uefryx7uje7'
)
cursor = cnx.cursor()

sql=( "INSERT INTO inscrit (username,lastname,age,number)VALUES (%s, %s, %s, %s)")
val = ('username', 'lastname', 'age','number')
cursor.execute(sql, val)
cnx.commit() 
        
 
flash("Employee Inserted Successfully")
 
return redirect(url_for('Index'))

cnx.commit()

print(cursor.rowcount, "record inserted.")


# Make sure data is committed to the database 
