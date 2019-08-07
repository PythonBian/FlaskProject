"""
项目管理文件
"""

from FlaskDirtory.models import models
from FlaskDirtory.views import app

if __name__ == "__main__":
    models.create_all()
    app.run()


