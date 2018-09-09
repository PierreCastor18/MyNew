from flask import Flask
from config import config
#使用flask_session扩展包， 将登陆信息存储到redis数据库中
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

#设计模式:工厂函数  :让app通过函数进行调用,可以动态的生产不同状态的app
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db = SQLAlchemy(app)
    # 初始化session 和程序实例进行关联
    Session(app)
    return app