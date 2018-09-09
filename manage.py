from flask import session
from info import create_app,db,models

#导入flask_script
from flask_script import Manager

#导入数据库迁移
from flask_migrate import Migrate,MigrateCommand

#调用生成的app，传入不同的配置信息
app = create_app('development')

#实例化管理对象
manage = Manager(app)
#此时db已经和程序进行关联了
Migrate(app,db)

#使用迁移框架
manage.add_command("db",MigrateCommand)


if __name__ == "__main__":
    # app.run()
    manage.run()