import MySQLdb
from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    con = MySQLdb.connect('192.168.1.191', 'root', '123', 'on_table')

    cur = con.cursor()
    qry = "select * from dark"
    cur.execute(qry)

    ver = cur.fetchall()
    return json.dumps(ver)

if __name__ == '__main__':
    app.run()