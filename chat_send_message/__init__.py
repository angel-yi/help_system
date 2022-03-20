from flask import Blueprint

chat_send_message_bp = Blueprint('chat_send_message', __name__)

# 这一行需要导入，否则无法引入
from . import views
