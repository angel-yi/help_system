from flask import Blueprint

admin_bp = Blueprint('admin', __name__)

# 这一行需要导入，否则无法引入
from . import views
