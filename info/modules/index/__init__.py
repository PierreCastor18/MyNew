
#导入蓝图
from flask import Blueprint

#创建蓝图对象,第一个参数是蓝图的名称
index_blue = Blueprint("index_blue",__name__)

from . import views