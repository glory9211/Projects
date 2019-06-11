import sqlite3


db_filename = 'test.db'


conn = sqlite3.connect(db_filename)

c = conn.cursor()

c.execute('create table accounts (name TEXT)')