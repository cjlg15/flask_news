from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask_session import Session  # 指定session保存的位置


class Config(object):
    """项目配置"""
    DEBUG = True

    SECRET_KEY = "4QYRhXCn0Cjnw19P8m99rjRRraI6FcAxEVD/BEJv7Z22eg78OZ+FkJAXLg3Gsic7"

    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:135254@127.0.0.1:3306/flask_news"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # Session配置
    # 指定session储存类型
    SESSION_TYPE = 'redis'
    # 开启sesssion签名，作用：保护session，对其进行加密
    SESSION_USE_SIGNER = True
    # 指定session 储存对象
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置session需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400*2


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


@app.route('/')
def index():
    session['name'] = 'yy'
    return '<h1>测试session写入到redis中</h1>'


if __name__ == '__main__':
    app.run()