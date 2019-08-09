"""
负责模型
"""
from app import models


class BaseModel(models.Model):
    __abstract__ = True #抽象表为True，代表当前类为抽象类，不会被创建
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    def save(self):
        db = models.session()
        db.add(self)
        db.commit()
    def delete_obj(self):
        db = models.session()
        db.delete(self)
        db.commit()

class User(BaseModel):
    __tablename__ = "user"
    username = models.Column(models.String(32))
    password = models.Column(models.String(32))
    identity = models.Column(models.Integer) #0 学员 #1 教师
    identity_id = models.Column(models.Integer,nullable=True)


class Students(BaseModel):
    """
    学员表
    """
    __tablename__ = "students"
    name = models.Column(models.String(32))
    age = models.Column(models.Integer)
    gender = models.Column(models.Integer,default = 13) #0 男 1女 -1 unknown


Stu_Cou = models.Table(
    "stu_cou",
    models.Column("id", models.Integer, primary_key=True, autoincrement=True),
    models.Column("course_id", models.Integer, models.ForeignKey("course.id")),
    models.Column("student_id", models.Integer, models.ForeignKey("students.id"))
)


class Course(BaseModel):
    """
    课程表
    """
    __tablename__ = "course"
    label = models.Column(models.String(32))
    description = models.Column(models.Text)

    to_teacher = models.relationship(
        "Teachers",  #映射表
        backref = "to_course_data", #反向映射字段，反向映射表通过该字段查询当前表内容
    ) #指向映射表字段

    to_student = models.relationship(
        "Students",
        secondary = Stu_Cou,
        backref = models.backref("to_course",lazy = "dynamic"), #stu_cou course
        lazy = "dynamic" #stu_cou student
        #select 访问该字段时候，加载所有的映射数据
        #joined  对关联的两个表students和stu_cou进行join查询
        #dynamic 不加载数据
    )


class Attendance(BaseModel):
    """
    考勤表，记录是否请假
    学员
    """
    __tablename__ = "attendance"
    att_time = models.Column(models.Date)
    status = models.Column(models.Integer,default = 1) #0 迟到  1 正常出勤  2 早退  3 请假  4 旷课
    student_id = models.Column(models.Integer, models.ForeignKey("students.id"))


class Grade(BaseModel):
    """
    成绩表
    课程，学员关联此表
    """
    __tablename__ = "grade"
    grade = models.Column(models.Float, default=0)
    course_id = models.Column(models.Integer, models.ForeignKey("course.id"))
    student_id = models.Column(models.Integer, models.ForeignKey("students.id"))


class Teachers(BaseModel):
    """
    教师
    老师与课程是多对一关系
    """
    __tablename__ = "teachers"
    name = models.Column(models.String(32))
    age = models.Column(models.Integer)
    gender = models.Column(models.Integer,default = 3)  # 0 男 1女 -1 unknown
    course_id = models.Column(models.Integer, models.ForeignKey("course.id")) #教师多对一 映射表是课程

