#配置文件
from redis import StrictRedis

class Config:

    DEBUG = None
    SECRET_KEY = 'gqpmIY5xGcS5EC8GiUecxAYr7DQjCmu1yyNcAk/NWXoKhxg+VE5+lw=='

    # 配置数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@localhost/MyNews"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 状态保持的session信息保存到redis数据库中
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host='127.0.0.1',port=6379)
    SESSION_USE_SIGNER = True       #对session信息进行签名
    PERMANENT_SESSION_LIFETIME = 86400  #设置session信息的有效期


#开发模式下的配置：继承自Config
class developmentConfig(Config):
    DEBUG = True

#生产模式下的配置：
class productionConfig(Config):
    DEBUG = False

#定义字典，映射不同的配置类信息
config = {
    'development': developmentConfig,
    'production': productionConfig
}
