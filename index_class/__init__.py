from flask import Blueprint

class_bp = Blueprint('index_class', __name__)

# 这一行需要导入，否则无法引入
from . import views
