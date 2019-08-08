import wtforms #定义字段
from flask_wtf import Form #定义表单
from wtforms import validators  #定义校验

class TeacherForm(Form):
    """
    form字段的参数
    label=None, 表单的标签
    validators=None, 校验，传入校验的方法
    filters=tuple(), 过滤
    description='',  描述
    id=None, html id
    default=None, 默认值
    widget=None,
    render_kw=None,
    """

    name = wtforms.StringField("教师姓名",
                               render_kw = {
                                   "class": "form-control",
                                   "placeholder": "教师姓名"
                               },
                               validators = [
                                   validators.DataRequired("姓名不可以为空")
                               ]
    )
    age = wtforms.IntegerField("教师年龄",
                               render_kw={
                                   "class": "form-control",
                                   "placeholder": "教师年龄"
                               },
                               validators=[
                                   validators.DataRequired("年龄不可以为空")
                               ]
    )
    gender = wtforms.StringField("教师性别",
                                render_kw = {
                                    "class": "form-control",
                                    "placeholder": "教师年龄"
                                },
                                validators=[
                                     validators.DataRequired("性别不可以为空")
                                ]
    )

    course = wtforms.SelectField(
        "学科",
        choices=[
            ("1", "PYTHON"),
            ("2", "PHP"),
            ("3", "JAVA"),
            ("4", "UI"),
            ("5", "WEB"),
        ],
        render_kw={
            "class": "form-control",
        }
    )