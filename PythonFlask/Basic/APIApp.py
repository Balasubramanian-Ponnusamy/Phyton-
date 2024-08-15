from flask import Flask, render_template, redirect, request
from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy import create_engine
import pyodbc 

blogs = Flask(__name__)
 
@blogs.route("/") #For default route
def main():
    mssqltips = []
    row = []
    cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};Server=SRINTE302;Database=DevTracket;User ID=ffteam;Password=FFteam$321')
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM ProductApiTable") 
    row = cursor.fetchone() 
    while row:
        print (row) 
        row = cursor.fetchone()

        mssqltips.append({"BlogId": row[0], "Username": row[1], "BlogTitle": row[2], "BlogDescription": row[3]})
  
    return render_template("BlogList.html",  mssqltips =  mssqltips)
 
if(__name__ == "__main__"):
    blogs.run() 