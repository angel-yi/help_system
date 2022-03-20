from flask import Blueprint

my_info_bp = Blueprint('my_info', __name__)

# 这一行需要导入，否则无法引入
from . import views
