from flask import Flask

import pymysql 
  

app = Flask(__name__)



@app.route('/')
def index():
    return f"Done!!"


@app.route('/test')
def mysqlconnect(): 
    # To connect MySQL database 
    try:

        conn = pymysql.connect( 
            host='mysql.railway.internal', 
            user='root',  
            password = "NBbvNdqSypiTHQVCTWAaXLXxrfbeStvK", 
            db='railway',
            port='3306'
        )
        
        cur = conn.cursor() 
        cur.execute("select @@version") 
        output = cur.fetchall() 
        print(output) 
    except Exception as e:
        prints(e)
        return e
      
    # To close the connection 
    conn.close()

    return "done"



if __name__ == '__main__':  
  app.run(debug = True)

