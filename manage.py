from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask_session import Session  # 指定session保存的位置
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand  # 迁移数据库
from config import Config


app = Flask(__name__)
# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启当前项目CSRF保护
CSRFProtect(app)
# 指定session初始化信息
Session(app)

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