import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == '__main__':
    
    folder_path = './files'
    
    conn = sqlite3.connect('database.db')
    
    with conn:
        con = conn.cursor()
        
        con.execute('DROP TABLE IF EXISTS files')
        con.execute('CREATE TABLE files (file_path TEXT NOT NULL)')
        
        while True:
            try:
                s = input()
                con.execute('INSERT INTO files (file_path) VALUES (?)',(s,))
            except:
                break