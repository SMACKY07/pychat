from flask import *
from db import register
import mysql.connector as m
import pyttsx3
import subprocess
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/registration")
def register1():
    return render_template("register.html")

@app.route("/done",methods = ['POST','GET'])
def done1():
    if request.method == 'POST':
        fname = request.form['fnm']
        lname = request.form['lnm']
        email = request.form['email']
        password = request.form['pswd']
        register(fname,lname,email,password)
        return "<script> alert('data inserted') </script>"
@app.route('/registerlogin',methods=['POST','GET'])    
def registerlogin():
    if request.method == 'POST':
        email = request.form['em']
        pswd = request.form['pswd']
        con = m.connect(host='localhost',user='root',password='smacky',database='register')
        cursor = con.cursor()
        cursor.execute("select email,password from tbl where email = %s and password = %s",(email,pswd))
        data = cursor.fetchone()
        if data:
            return render_template("main.html")
        else:
            return "<script> alert('incorrect username and password')</script>"
@app.route('/speak')
def speak():
    subprocess.call(['python','vcc.py'])
    




if __name__ =='__main__':
    app.run(host='localhost',port='2002',debug=True)