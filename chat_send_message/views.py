# coding:utf-8

from flask import render_template, request

from . import chat_send_message_bp


# 发送消息页视图函数
@chat_send_message_bp.route('/chat_send/send_message', methods=["POST"])
def chat_send_message_profile():
    if request.method == 'POST':
        print(request.form.get('us_message'))
    return render_template("chat.html")
