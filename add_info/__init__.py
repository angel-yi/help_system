from flask import Blueprint

add_info_bp = Blueprint('add_info', __name__)

# 这一行需要导入，否则无法引入
from . import views
