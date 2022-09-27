import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Tables (name, senha, email, posy) VALUES (?, ?, ?, ?)",
                                ('Pedro', '545700', 'pedropucci7@hotmail.com', '2') 
                                )

cur.execute("INSERT INTO Tables (name, senha, email, posy) VALUES (?, ?, ?, ?)",
                                ('Lucas', 'sonaoflol', 'lucasuchiha@gmail.com', '1')
                                )

connection.commit()
connection.close()  