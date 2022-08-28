from flask import Flask, render_template, request
from markupsafe import escape
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/sobre')
def sobre():
  return render_template("sobre.html")

@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Entra pelo Form"
     
    if request.method == 'POST':
        name = request.form['name']
        idade = request.form['idade']
        email = request.form['email']
        endereco = request.form['endereco']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO flask_table VALUES(%s,%s,%s,%s)''',(name,idade,email,endereco))
        mysql.connection.commit()
        cursor.close()
        return "Show de bola"

if __name__ == "__main__":
  app.run(debug=True)