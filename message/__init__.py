from flask import Blueprint

message_bp = Blueprint('message', __name__)

# 这一行需要导入，否则无法引入
from . import views
