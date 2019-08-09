"""
多蓝图命令行模式 蓝图2
"""
from flask import Blueprint


simple_blueprint2 = Blueprint("simple_page2",__name__) #创建蓝图

#bluePrint的路由和视图
@simple_blueprint2.route("/index2")
def index():
    return "hello world2"