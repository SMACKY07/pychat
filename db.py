import pymysql

def register(fname,lname,email,password):
    con = pymysql.connect(host="localhost",user="root",password="smacky",database="register")
    cursor  = con.cursor()
    cursor.execute("insert into tbl(fname,lname,email,password)values(%s,%s,%s,%s)",(fname,lname,email,password))
    con.commit()
    cursor.close()
    con.close()
    return 1



