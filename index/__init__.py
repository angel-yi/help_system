from flask import Blueprint

index_bp = Blueprint('index', __name__)

# 这一行需要导入，否则无法引入
from . import views
