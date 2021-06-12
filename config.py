from redis import StrictRedis


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
