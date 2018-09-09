from flask import Flask,session
from config import Config
from flask_sqlalchemy import SQLAlchemy
#使用flask_session扩展包， 将登陆信息存储到redis数据库中
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

#配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:mysql@localhost/MyNews"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#初始化session 和程序实例进行关联
Session(app)


@app.route("/")
def index():

    session["name"] = '2018'
    return "index"

if __name__ == "__main__":
    app.run()