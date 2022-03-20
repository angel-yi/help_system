# coding:utf-8

import datetime
import random

from flask import render_template, url_for, redirect, request, session, flash

from sql_cx import SqlCx
from . import add_info_bp


# 发布信息
@add_info_bp.route('/add_info', methods=["GET"])
def add_info_profile():
    user_id = session.get('user')
    if user_id:
        # 返回发布页面
        sql = f"SELECT * FROM help_system.info_class;"
        data = SqlCx(sql)
        print(data)
        return render_template("add_info_2.html", info_class=data)
    else:
        flash('请您先登录！')
        return redirect(url_for('my_info.login_profile'))


# 发布信息
@add_info_bp.route('/add_info/add_info', methods=["POST"])
def add_file_profile():
    # 返回发布页面
    img = request.files.get('image')
    title = request.form.get('title')
    content = request.form.get('content')
    info_class = request.form.get('info_class')
    print(img)
    print(title)
    print(content)
    print(info_class)
    user_id = session.get('user')
    da = datetime.datetime.now()
    try:
        path = 'static/user_images/'
        now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        random_num = random.randint(0, 100)
        if random_num <= 10:
            random_num = str(0) + str(random_num)
        unique_name = str(now_time) + str(random_num)
        ext = str(img.filename).split('.', 1)[1]
        file_path = path + unique_name + '.' + ext
        img.save(file_path)
        info_title = title
        info_content = str(content).replace(' ', '').replace('\n', '').replace('\r', '')
        info_image = '../' + file_path
        info_user_id = user_id
        info_date = da
        info_state = 0
        sql = f"INSERT INTO info_data (`info_id`, `info_title`, `info_content`, `info_image`, `info_date`, `info_state`, `info_user_id`, `info_class`) VALUE (null, '{info_title}', '{info_content}', '{info_image}', '{info_date}', {info_state}, '{info_user_id}', {info_class})"
        print(sql)
        SqlCx(sql)
        # app.help_database.session.add(info)
        # app.help_database.session.commit()
        return redirect('/')
    except:
        info_title = title
        info_content = content
        info_user_id = user_id
        info_date = da
        info_state = 0
        sql = f"INSERT INTO info_data (`info_id`, `info_title`, `info_content`, `info_image`, `info_date`, `info_state`, `info_user_id`, `info_class`) VALUE (null, '{info_title}', '{info_content}', '', '{info_date}', {info_state}, '{info_user_id}', {info_class})"
        print(sql)
        SqlCx(sql)
        return redirect('/')


@add_info_bp.route('/edit_info/<int:info_id>', methods=['GET'])
def edit_info_profile(info_id):
    user_id = session.get('user')
    if user_id:
        # 返回发布页面
        sql = f"SELECT * FROM help_system.info_data, info_class where info_id={info_id} and info_data.info_class=info_class.id"
        data = SqlCx(sql)
        print(data)
        sql = f"SELECT * FROM help_system.info_class;"
        info_class = SqlCx(sql)
        print(info_class)
        return render_template("edit_info.html", info_data=data[0], info_class=info_class)
    else:
        flash('请您先登录！')
        return redirect(url_for('my_info.login_profile'))


@add_info_bp.route('/edit_info/edit_info', methods=['POST'])
def edit_file_profile():
    info_id = request.form.get('info_id')
    img = request.files.get('image')
    title = request.form.get('title')
    content = request.form.get('content')
    info_class = request.form.get('info_class')
    user_id = session.get('user')
    da = datetime.datetime.now()
    info_title = title
    info_content = content
    try:
        path = 'static/user_images/'
        now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        random_num = random.randint(0, 100)
        if random_num <= 10:
            random_num = str(0) + str(random_num)
        unique_name = str(now_time) + str(random_num)
        ext = str(img.filename).split('.', 1)[1]
        file_path = path + unique_name + '.' + ext
        img.save(file_path)
        info_image = '../' + file_path
        sql = f"UPDATE info_data SET info_title='{info_title}', info_content='{info_content}', info_image='{info_image}', info_class={info_class}, info_examine=0 WHERE info_id={info_id}"
        print(sql)
        SqlCx(sql)
    except:
        sql = f"UPDATE info_data SET info_data.info_title='{info_title}', info_data.info_content='{info_content}', info_data.info_class={info_class}, info_examine=0 WHERE info_data.info_id={info_id}"
        print(sql)
        SqlCx(sql)
    return redirect(url_for('my_info.my_info_data_profile'))


@add_info_bp.route('/delete_info/<int:info_id>', methods=['GET'])
def delete_info_profile(info_id):
    user_id = session.get('user')
    if user_id:
        # 返回发布页面
        sql = f"delete FROM help_system.info_data where info_id={info_id}"
        data = SqlCx(sql)
        print(data)
        return redirect(url_for('my_info.my_info_data'))
    else:
        flash('请您先登录！')
        return redirect(url_for('my_info.login_profile'))
