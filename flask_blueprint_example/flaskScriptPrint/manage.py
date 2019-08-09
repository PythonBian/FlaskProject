"""
多蓝图命令模式 应用
"""
from flask import Flask
from flask_script import Manager

from BluePrint1 import simple_blueprint1
from BluePrint2 import simple_blueprint2

app = Flask(__name__)
app.register_blueprint(simple_blueprint1)
app.register_blueprint(simple_blueprint2)

manage = Manager(app)

if __name__ == "__main__":
    manage.run()
