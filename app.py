from flask import Flask

import pymysql 
  

app = Flask(__name__)



@app.route('/')
def index():
    return f"Done!!"


@app.route('/test')
def mysqlconnect(): 
    # To connect MySQL database 
    conn = pymysql.connect( 
        host='mysql.railway.internal', 
        user='root',  
        password = "NBbvNdqSypiTHQVCTWAaXLXxrfbeStvK", 
        db='railway',
    )
      
    cur = conn.cursor() 
    cur.execute("select @@version") 
    output = cur.fetchall() 
    print(output) 
      
    # To close the connection 
    conn.close() 



if __name__ == '__main__':  
  app.run(debug = True)

