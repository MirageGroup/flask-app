import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Tables (name, senha, email) VALUES (?, ?, ?)",
                                ('Pedro', '545700', 'pedropucci7@hotmail.com') 
                                )

cur.execute("INSERT INTO Tables (name, senha, email) VALUES (?, ?, ?)",
                                ('Lucas', 'sonaoflol', 'lucasuchiha@gmail.com')
                                )

connection.commit()
connection.close()  