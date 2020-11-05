from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:devops@35.246.67.5/flaskDemo"
app.config['SECRET_KEY'] = 'hndsnbaiohewdiowahnk'
db = SQLAlchemy(app)

from application import routes
