from flask import session
from info import create_app

#导入flask_script
from flask_script import Manager

#调用生成的app，传入不同的配置信息
app = create_app('development')

#实例化管理对象
manage = Manager(app)


@app.route("/")
def index():

    session["name"] = '2018'
    return "index"

if __name__ == "__main__":
    # app.run()
    manage.run()