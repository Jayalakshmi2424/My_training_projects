'''Login Authentication using python flask and postgres db '''
''' email is a primary key in table "register"'''
'''table's column names are username,age,email and password'''

from flask import Flask, render_template, request, url_for, redirect
import psycopg2
from psycopg2 import Error

app = Flask(__name__)

#user registration page
@app.route('/')
def register():
    return render_template("register.html")

#rendering login page after successful registration
@app.route('/login', methods=['GET','POST'])
def login():

#request inputs from registration page
    username = request.args.get('username')
    age = request.args.get('age')
    email = request.args.get('email')
    password = request.args.get('password')
    records_to_insert=(username, age, email, password) 
    
    #postgres db connection   
    try:
        connection = psycopg2.connect(user="postgres",
                                      password=#password,
                                      host="127.0.0.1",
                                      port="5432",
                                      database=#dbname)

        cursor = connection.cursor()
        
        #values insertion into table
        postgres_insert_query = '''INSERT INTO register (username , age, email, password) VALUES (%s,%s,%s,%s)'''
         	
        cursor.execute(postgres_insert_query, records_to_insert)

        connection.commit()
        
        print("values successfully inserted\n")
        
    except (Exception, Error) as error:
   	 print("Error while connecting to PostgreSQL\n", error)
   	 
    finally:
    	 if (connection):
    	        cursor.close()
    	        connection.close()
    	        print("PostgreSQL connection is closed")
   
    return render_template("login.html")


#user authentication                           
@app.route('/authenticate', methods=['GET','POST'])
def authenticate():
    email = request.args.get('email')
    password = request.args.get('password')
   
    try:
        connection = psycopg2.connect(user="postgres",
                                      password=#password,
                                      host="127.0.0.1",
                                      port="5432",
                                      database=#dbname)


        cursor = connection.cursor()
        #email verification
        cursor.execute('''SELECT email,password from register where email = '%s' '''%email)
        var1=cursor.fetchone()
        if var1==None:	
        	 warning="You are not a user!!!, Register here"
        	 return render_template("register.html",warning=warning)
        connection.commit()
        cursor.execute('''SELECT password from register where email= '%s'  '''%email)
        var2=cursor.fetchone()
        var1=var1[0].replace(",","")
        var2=var2[0].replace(",","")
        print(var1)
        print(var2)
        #password verification
        if password!=var2:
        	return '''<html><center><br><br><h2>Incorrect Password !!!</h2><center></html>'''
        else:
        	cursor.execute('''SELECT username from register where email = '%s'  '''%email)
        	v=cursor.fetchone()
        	v=v[0].replace(",","")
        	return render_template("authenticate.html",username=v)
        	
    except (Exception, Error) as error:
    	return print("Error while connecting to PostgreSQL", error)
    finally:
    	 if (connection):
    	        cursor.close()
    	        connection.close()
    	        print("PostgreSQL connection is closed")
  
if __name__ == "__main__":
    app.run(debug=True, port=8080)
