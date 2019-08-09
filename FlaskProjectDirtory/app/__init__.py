from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

import pymysql
pymysql.install_as_MySQLdb()

#惰性加载
csrf = CSRFProtect()
models = SQLAlchemy()

def create_app(config_name):
    #创建app实例
    app = Flask(__name__)
    app.config.from_object("settings.DebugConfig")

    #app惰性加载插件
    csrf.init_app(app) #惰性加载
    models.init_app(app)

    #注册蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
