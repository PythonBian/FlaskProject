import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "bjh123" #用来生成session_id和之后csrf_token,
    CACHE_TYPE = "simple"

class DebugConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "Student_test.sqlite")
    #SQLALCHEMY_DATABASE_URI = "mysql://root:123@localhost/school"


class OnlineConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "Student_test.sqlite")

