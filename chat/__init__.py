from flask import Blueprint

chat_bp = Blueprint('chat', __name__)

# 这一行需要导入，否则无法引入
from . import views
