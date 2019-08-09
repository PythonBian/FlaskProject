"""
flask script 官方案例
"""
from flask import Flask
from flask_script import Manager

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

manager = Manager(app) #对app进行命令行序列化


if __name__ == "__main__":
    manager.run()  #启动flask manage，manage启动app
