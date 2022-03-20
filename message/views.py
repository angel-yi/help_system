# coding:utf-8
import datetime
from flask import render_template, session, flash, redirect, url_for, request

from mgc import mgc_jc
from sql_cx import SqlCx
from . import message_bp


# 消息页视图函数
@message_bp.route('/message', methods=["GET"])
def message_profile():
    user_account = session.get('user')
    if user_account:
        sql = f"select * from info_message, users_data where info_message.user_id='{user_account}' and info_message.info_user_id=users_data.user_account order by info_message.send_date desc"
        message = SqlCx(sql)
        print('[message]', message)
        return render_template("message.html", message=message)
    else:
        flash('请登录后再查看消息！')
        return redirect(url_for('my_info.login_profile'))


@message_bp.route('/message_detail/<int:message_id>', methods=["GET"])
def message_detail_profile(message_id):
    # http://127.0.0.1:5000/message_detail/5
    user_account = session.get('user')
    if user_account:
        sql = f"select * from info_message, users_data where message_id={message_id} and info_message.info_user_id=users_data.user_account"
        message = SqlCx(sql)
        print('[message]', message)
        tel_sql = f"select user_tel from users_data where user_account='{user_account}'"
        tel = SqlCx(tel_sql)
        return render_template("message_detail.html", message=message[0], tel=tel[0])
    else:
        flash('请登录后再查看消息！')
        return redirect(url_for('my_info.login_profile'))


@message_bp.route('/yz_message', methods=["POST"])
def yz_message_profile():
    if session.get('user'):
        user_id = session.get('user')
        message_dict = request.form.to_dict()
        info_id = message_dict['info_id']
        info_user_id = message_dict['user_id']
        # sql = f"select * from info_data where info_id={info_id}"
        # info_user_id = SqlCx(sql)
        message = message_dict['message']
        message = mgc_jc(message)
        da = datetime.datetime.now()
        sql = f"insert into info_message value (null, {info_id}, '{user_id}', '{info_user_id}', '{message}', '{da}', 2)"
        print(sql)
        SqlCx(sql)
        print('[message]: ', message)
        return redirect(url_for('detail.detail_profile', info_id=info_id))
    else:
        flash('请登录后再进行评论！')
        return redirect(url_for('my_info.login_profile'))


@message_bp.route('/hl_message/<int:message_id>', methods=["GET"])
def hl_message_profile(message_id):
    sql = f"update info_message set message_status=1 where message_id={message_id}"
    SqlCx(sql)
    return redirect(url_for('message.message_profile'))
