from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as fp:
    connection.executescript(fp.read())

cur = connection.cursor()

cur.execute("INSERT INTO files (file_path) VALUES (?)", ('//host1/path1.ext',))
cur.execute("INSERT INTO files (file_path) VALUES (?)", ('//host2/path2.ext',))


connection.commit()
connection.close()