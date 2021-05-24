from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


class Config(object):
    """项目配置"""
    DEBUG = True

    # 为数据库添加配置
    SQLAlchemy_DATABASE_URI = "mysql://root:135254@127.0.0.1:3306/flask_news"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
# 加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)


@app.route('/')
def index():
    pass


if __name__ == '__main__':
    app.run()