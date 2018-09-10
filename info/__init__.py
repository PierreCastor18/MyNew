from flask import Flask
from config import config
#使用flask_session扩展包， 将登陆信息存储到redis数据库中
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
#导入日志
import logging
#日志处理模块
from logging.handlers import RotatingFileHandler

def setup_log(config_name):
    # 设置日志的记录等级
    logging.basicConfig(level=logging.DEBUG)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)

#先实例化sqlalchemy对象
db = SQLAlchemy()

#设计模式:工厂函数  :让app通过函数进行调用,可以动态的生产不同状态的app
def create_app(config_name):

    setup_log(config_name)
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    #让sqlalchemy对象和程序进行关联
    db.init_app(app)    #传入app

    # 初始化session 和程序实例进行关联
    Session(app)
    #注册蓝图
    from info.modules.index import index_blue
    app.register_blueprint(index_blue)

    return app