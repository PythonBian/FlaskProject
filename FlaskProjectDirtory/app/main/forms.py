import wtforms #定义字段
from flask_wtf import FlaskForm #定义表单 由于版本原因，将FORM改为FlaskForm
from wtforms import validators  #定义校验

# forms当中禁止查看数据库，数据库查询被认为视图功能
# from FlaskDirtory.models import Course
#
# course_list = [(c.id,c.label) for c in Course.query.all()]
course_list = []
class TeacherForm(FlaskForm):
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
    gender = wtforms.SelectField(
        "性别",
        choices=[
            ("1", "男"),
            ("2", "女")
        ],
        render_kw={
            "class": "form-control",
        }
    )

    course = wtforms.SelectField(
        "学科",
        choices = course_list,
        render_kw={
            "class": "form-control",
        }
    )