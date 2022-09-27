from flask import Flask, render_template, request, redirect
from markupsafe import escape
#from flask_mysqldb import MySQL
import sqlite3

app = Flask(__name__)

#app.config['MYSQL_HOST'] = '127.0.0.1'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'flask'
#
#mysql = MySQL(app)

def get_db_connection():
  conn = sqlite3.connect('database.db')
  conn.row_factory = sqlite3.Row
  return conn

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/sobre')
def sobre():
  return render_template("sobre.html")

@app.route('/form')
def form():
  return render_template('form.html')

@app.route('/sqlite', methods = ['POST', 'GET'])
def sqlite():
  if request.method == 'POST':
    conn = get_db_connection()
    name = request.form['name']
    senha = request.form['senha']
    email = request.form['email']
    posicao = request.form['posicao']
    conn.execute('INSERT INTO Tables (name, senha, email, posy) VALUES (?, ?, ?, ?)', (name, senha, email, posicao))
    conn.commit()
    conn.close()
    return redirect('/sqlite')
  else:
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM Tables ORDER BY posy ASC').fetchall()
    conn.close()
    return render_template('sqlite3.html', users=users)

@app.route('/sqlite_delete/<int:userid>', methods = ['POST'])
def sqlite_delete(userid):
  conn = get_db_connection()
  conn.execute(f'DELETE FROM Tables WHERE id = {userid}')
  conn.commit()
  conn.close()
  return redirect('/sqlite')
 
@app.route('/sqlite_edit/<int:userid>')
def sqlite_edit(userid):
  conn = get_db_connection()
  user = conn.execute(f'SELECT * FROM Tables WHERE id = {userid}').fetchall()
  conn.close()
  return render_template('update.html', user=user)

#@app.route('/login', methods = ['POST', 'GET'])
#def login():
#    if request.method == 'GET':
#        return "Entra pelo Form"
#     
#   if request.method == 'POST':
#        name = request.form['name']
#        idade = request.form['idade']
#       email = request.form['email']
#       endereco = request.form['endereco']
#       cursor = mysql.connection.cursor()
#       cursor.execute(''' INSERT INTO flask_table VALUES(%s,%s,%s,%s)''',(name,idade,email,endereco))
#       mysql.connection.commit()
#        cursor.close()
#        return "Show de bola"

if __name__ == "__main__":
  app.run(debug=True)