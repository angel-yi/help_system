# coding:utf-8
import time
from flask import render_template, url_for, redirect

import app
from . import chat_bp


# 聊天页视图函数
@chat_bp.route('/chat', methods=["GET"])
def chat_profile():
    info_data = app.InfoData.query.limit(30).all()
    return render_template("chat.html", info_data=info_data)


@chat_bp.route('/chat_create/<int:user_id>', methods=["GET"])
def chat_create_profile(user_id):
    receive_user_id = 1
    id_list = [receive_user_id, user_id]
    hash_recevice_user_id = hash(str(id_list))
    print(hash_recevice_user_id)
    chat = app.ChatData()
    chat.chat_id = None
    chat.chat_hash = str(hash_recevice_user_id)
    chat.chat_date = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    chat.chat_content = '开始聊天吧 请文明交流'
    chat.chat_state = '0'
    app.help_database.session.add(chat)
    app.help_database.session.commit()
    return redirect(url_for('chat.chat_profile'))
