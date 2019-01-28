from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 設定資料庫位置，並建立 app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:0933822291@localhost:3306/members'
# app.config.from_object('flaskconfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)