"""
负责视图和路由
"""
import hashlib

from flask import request
from flask import redirect
from flask import render_template

from FlaskDirtory.main import app
from FlaskDirtory.models import *
from FlaskDirtory.main import session

def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()

@app.route("/register/",methods=["GET","POST"])
def register():
    if request.method == "POST":
        form_data = request.form
        username = form_data.get("username")
        password = form_data.get("password")
        identity = form_data.get("identity")
        user = User()
        user.username = username
        user.password = setPassword(password)
        user.identity = int(identity)
        user.save()
        return redirect("/login/")
    return render_template("register.html", **locals())


@app.route("/login/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        form_data = request.form
        username = form_data.get("username")
        password = form_data.get("password")

        user = User.query.filter_by(username = username).first()
        if user:
            send_password = setPassword(password)
            db_password = user.password
            if send_password == db_password:
                # 进行跳转
                response = redirect("/index/")
                #设置cookie
                response.set_cookie("username",username)
                response.set_cookie("user_id",str(user.id))
                #设置session
                session["username"] = username
                #返回跳转
                return response
    return render_template("login.html", **locals())



@app.route("/index/",methods=["GET","POST"])
def index():
    students = Students.query.all()
    response = render_template("students_list.html", **locals())
    #response.set_cookie("")
    return response

@app.route("/logout/",methods=["GET","POST"])
def logout():
    students = Students.query.all()
    response = render_template("students_list.html", **locals())
    #response.set_cookie("")
    return response


@app.route("/student_list/",methods=["GET","POST"])
def student_list():
    students = Students.query.all()
    response = render_template("students_list.html", **locals())
    #response.set_cookie("")
    return response

