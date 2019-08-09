"""
多蓝图模式 应用
"""
from flask import Flask
from twoBluePrint.BluePrint1 import simple_blueprint1
from twoBluePrint.BluePrint2 import simple_blueprint2

app = Flask(__name__)
app.register_blueprint(simple_blueprint1)
app.register_blueprint(simple_blueprint2)

if __name__ == "__main__":
    app.run()
