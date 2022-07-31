from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/',methods=["GET","POST"])
def index():
    uslovie = ""
    if request.method == 'POST':
        poisk = request.form.get('poisk',"")
        for u in poisk.split():
            uslovie += " AND file_path LIKE '%" + u + "%'"
        
    conn = get_db_connection()
    rows = conn.execute('SELECT * FROM files WHERE 1' + uslovie).fetchall()
    conn.close()
    return render_template('index.html',uslovie=uslovie,rows=rows)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)