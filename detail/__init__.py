from flask import Blueprint

detail_bp = Blueprint('detail', __name__)

# 这一行需要导入，否则无法引入
from . import views
