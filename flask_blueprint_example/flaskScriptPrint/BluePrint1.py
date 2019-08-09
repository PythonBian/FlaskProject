"""
多蓝图命令行模式 蓝图1
"""
from flask import Blueprint


simple_blueprint1 = Blueprint("simple_page1",__name__) #创建蓝图

#bluePrint的路由和视图
@simple_blueprint1.route("/index1")
def index():
    return "hello world1"