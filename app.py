from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask import request
import mysql.connector
import json
import paramiko
app = Flask(__name__)
app.secret_key = "Secret Key"
# Database Configuration With Mysql

cnx = mysql.connector.connect(
  host='bs4ttoxa3uefryx7uje7-mysql.services.clever-cloud.com',
  user='ujypevobdznoejre',
  password='0f8Z8R1fpniQ0GkOxeYK',
  database='bs4ttoxa3uefryx7uje7'
)
cursor = cnx.cursor()
@app.route('/')
def home():
   return render_template('index.html')

#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        username = request.form['username']
        lastname = request.form['lastname']
        age = request.form['age']
        number = request.form['number']
        
        sql=( "INSERT INTO inscrit (username,lastname,age,number)VALUES (%s, %s, %s, %s)")
        val = ('username', 'lastname', 'age','number')
       #cursor.execute(sql, val)
       #cnx.commit() 
        flash("Employee Inserted Successfully")
        return redirect(url_for('Index'))
      
       

if __name__ == '__main__':
   app.run(debug = True, port=80)