from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/sobre')
def sobre():
  return render_template("sobre.html")

if __name__ == "__main__":
  app.run(debug=True)