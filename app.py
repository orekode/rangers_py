from flask import Flask
# from flask_mysqldb import MySQL

app = Flask(__name__)

 
# app.config['MYSQL_HOST'] = 'https://rapidcrewtech.com/'
# app.config['MYSQL_USER'] = 'rapidcre_rangers'
# app.config['MYSQL_PASSWORD'] = 'rangers@hack@thon'
# app.config['MYSQL_DB'] = 'rapidcre_rangers'
 
# mysql = MySQL(app)


@app.route('/')
def index():
    # cursor = mysql.connection.cursor()
    # cursor.execute(''' INSERT INTO test VALUES(%s,%s)''',('david','12'))
    # mysql.connection.commit()
    # cursor.close()
    # print()
    return f"Done!!"

#implement bulk upload
#       save file

#   make request to classifier

#   make request to understanding model

#   connect to a mysql (test connection)


if __name__ == '__main__':  
  app.run(debug = True)

