from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand  # 迁移数据库
from info import app, db


manager = Manager(app)
# 将app 和 db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session['name2'] = 'jj'
    return '<h1>测试session写入到redis中</h1>'


if __name__ == '__main__':
    manager.run()