import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_PATH")

db = SQLAlchemy(app)

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/cam')
def webinar():
    return render_template("webinar.html")

@app.route('/demo')
def demo():
    return render_template("demo.html")

if __name__ == '__main__':
    app.run(debug=True, port=5050)
