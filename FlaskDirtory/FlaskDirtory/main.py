import os

import pymysql
from flask import Flask
from flask import session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect #CsrfProtect在1.0之后移除

#之前好多flask插件都存放在ext模块下
#后来独立出来，我们以flask_session为例
#from flask_session import Session

pymysql.install_as_MySQLdb()

app = Flask(__name__)

csrf = CSRFProtect(app)

app.config.from_object('config.DebugConfig')

models = SQLAlchemy(app) #关联sqlalchemy和flask应用





# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(BASE_DIR,"Student.sqlite")
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

#app.config.from_pyfile("settings.py")
