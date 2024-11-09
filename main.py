import os
from dotenv import load_dotenv
from flask import Flask, load_template
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_PATH")

db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return os.getenv("DB_PATH")


if __name__ == '__main__':
    app.run(debug=True)
