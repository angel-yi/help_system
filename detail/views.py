# coding:utf-8
import datetime
from flask import render_template, request, session, redirect, url_for, flash

from mgc import mgc_jc
from sql_cx import SqlCx
from . import detail_bp


@detail_bp.route('/test', methods=["GET"])
def test():
    return render_template("test.html")


# 详情视图函数
@detail_bp.route('/detail/<int:info_id>', methods=["GET"])
def detail_profile(info_id):
    sql = f"select * from info_data, info_class where info_data.info_class=info_class.info_class_value and info_id={info_id}"
    info_data = SqlCx(sql)
    print('info_data', info_data)
    sql = f"select * from users_data where user_account='{info_data[0]['info_user_id']}'"
    user_data = SqlCx(sql)
    print('user_data', user_data)
    # info_data.info_date = str(info_data.info_date)[5:16]
    # print('[info_data]', info_data.info_id)
    sql = f"select * from info_comment, users_data where info_comment.user_id=users_data.user_account and info_comment.info_id={info_id}"
    comment = SqlCx(sql)
    print('[comment]: ', comment)
    return render_template("detail.html", info=info_data[0], user=user_data[0], comment=comment)


@detail_bp.route('/comment/<int:info_id>', methods=['POST'])
def comment_profile(info_id):
    if session.get('user'):
        user_id = session.get('user')
        comment_dict = request.form.to_dict()
        message = comment_dict['comment']
        message = mgc_jc(message)
        da = datetime.datetime.now()
        sql = f"insert into info_comment value (null, {info_id}, '{user_id}', '{message}', '{da}')"
        SqlCx(sql)
        print('[message]: ', message)
        return redirect(url_for('detail.detail_profile', info_id=info_id))
    else:
        flash('请登录后再进行评论！')
        return redirect(url_for('my_info.login_profile'))


@detail_bp.route('/send_message', methods=['POST'])
def send_message_profile():
    if session.get('user'):
        user_id = session.get('user')
        message_dict = request.form.to_dict()
        info_id = message_dict['info_id']
        sql = f"select * from info_message where info_id='{info_id}' and user_id='{user_id}'"
        data = SqlCx(sql)
        if data:
            return redirect(url_for('detail.detail_profile', info_id=info_id))
        else:
            sql = f"select * from info_data where info_id={info_id}"
            info_user_id = SqlCx(sql)
            message = message_dict['message']
            message = mgc_jc(message)
            print(message)
            da = datetime.datetime.now()
            sql = f"insert into info_message value (null, {info_id}, '{user_id}', '{info_user_id[0]['info_user_id']}', '{message}', '{da}', 0)"
            print(sql)
            SqlCx(sql)
            sql = f"insert into users_like value (null , '{user_id}', {info_id}, '{da}')"
            SqlCx(sql)
            print('插入成功')
            print('[message]: ', message)
            return redirect(url_for('detail.detail_profile', info_id=info_id))
    else:
        flash('请登录后再进行评论！')
        return redirect(url_for('my_info.login_profile'))
