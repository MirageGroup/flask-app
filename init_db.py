import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Tables (name, senha, email, posx, posy) VALUES (?, ?, ?, ?, ?)",
                                ('Pedro', '545700', 'pedropucci7@hotmail.com', '1', '1') 
                                )

cur.execute("INSERT INTO Tables (name, senha, email, posx, posy) VALUES (?, ?, ?, ?, ?)",
                                ('Lucas', 'sonaoflol', 'lucasuchiha@gmail.com', '3', '1')
                                )

cur.execute("INSERT INTO Tables (name, senha, email, posx, posy) VALUES (?, ?, ?, ?, ?)",
                                ('Matheus', 'senhamatheus', 'matheus@gmail.com', '2', '2')
                                )

cur.execute("INSERT INTO Tables (name, senha, email, posx, posy) VALUES (?, ?, ?, ?, ?)",
                                ('Gustavo', 'senhagustavo', 'gustavo@gmail.com', '4', '2')
                                )
connection.commit()
connection.close()  