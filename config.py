#配置文件
from redis import StrictRedis

class Config:
    DEBUG = True
    SECRET_KEY = 'gqpmIY5xGcS5EC8GiUecxAYr7DQjCmu1yyNcAk/NWXoKhxg+VE5+lw=='

    # 状态保持的session信息保存到redis数据库中
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host='127.0.0.1',port=6379)
    SESSION_USE_SIGNER = True       #对session信息进行签名
    PERMANENT_SESSION_LIFETIME = 86400  #设置session信息的有效期