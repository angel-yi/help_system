# coding: utf-8
import datetime
import os
import random
from flask import render_template, url_for, redirect, request, session, flash

import dw
from sql_cx import SqlCx
from . import admin_bp


@admin_bp.route('/admin_profile', methods=['GET'])
def admin_profile():
    path = os.getcwd()
    print(path)
    try:
        os.remove(path + r'\templates\admin\1.html')
        os.remove(path + r'\templates\admin\2.html')
    except:
        print('删除失败')
    dw.info_count()
    dw.user_count()
    if session.get('admin_user'):
        user = session.get('admin_user')
        return render_template('admin/admin_index.html', user=user)
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/admin_profile_login', methods=['GET', 'POST'])
def admin_profile_login_profile():
    if request.method == 'GET':
        return render_template('admin/admin_login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        sql = f"SELECT * FROM admin_data where username='{username}' and username='{password}';"
        user_data = SqlCx(sql)
        if user_data:
            session['admin_user'] = username
            return redirect(url_for('admin.admin_profile'))
        else:
            flash('账户名或密码错误')
            return redirect(url_for('admin.admin_profile_login_profile'))


@admin_bp.route('/info_manage', methods=['GET'])
@admin_bp.route('/info_manage/<int:page>', methods=['GET'])
def admin_info_manage_profile(page=1):
    if session.get('admin_user'):
        a = (page - 1) * 7
        b = (page) * 7
        sql = f"select * from info_data, info_class where info_data.info_class=info_class.id order by info_data.info_date desc limit {a}, 7"
        data = SqlCx(sql)
        sql = "select * from info_data, info_class where info_data.info_class=info_class.id"
        data_count = SqlCx(sql)
        if int(len(data_count) / 7) > len(data_count) / 7:
            page_num = int(len(data_count) / 7)
        else:
            page_num = int(len(data_count) / 7)
        sql = f"SELECT * FROM help_system.info_class;"
        info_class = SqlCx(sql)
        user = session.get('admin_user')
        return render_template('admin/admin_info_manage.html', data=data, page=page, page_num=page_num,
                               info_class=info_class, user=user)
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/admin_edit_info', methods=['POST'])
def admin_edit_info():
    if session.get('admin_user'):
        info_id = request.form.get('info_id')
        title = request.form.get('bj_biaoti')
        content = request.form.get('bj_neirong')
        user = request.form.get('bj_yonghu')
        info_class = request.form.get('info_class')
        print(title, content, user, info_class)
        sql = f"UPDATE info_data SET info_data.info_title='{title}', info_data.info_content='{content}', info_data.info_class={info_class} WHERE info_data.info_id={info_id}"
        print(sql)
        SqlCx(sql)
        return redirect(url_for('admin.admin_info_manage_profile'))
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/delete_info', methods=['POST'])
def delete_info_profile():
    if session.get('admin_user'):
        if request.method == 'POST':
            info_id = request.form.get('info_id')
            print(info_id)
            sql = f"delete FROM info_data where info_id={info_id}"
            SqlCx(sql)
            return redirect(url_for("admin.admin_info_manage_profile"))
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/user_manage', methods=['GET'])
@admin_bp.route('/user_manage/<int:page>', methods=['GET'])
def admin_user_manage_profile(page=1):
    if session.get('admin_user'):
        a = (page - 1) * 7
        b = (page) * 7
        sql = f"-- SELECT info_user_id, COUNT(info_id) AS info_count,users_data.`*` FROM info_data, users_data WHERE info_data.info_user_id=users_data.user_account GROUP BY info_user_id ORDER BY users_data.user_reg_date DESC LIMIT {a},7"
        sql = f"select * from users_data ORDER BY users_data.user_reg_date DESC LIMIT {a},7"
        data = SqlCx(sql)
        sql = f"select * from users_data"
        data_count = SqlCx(sql)
        print(data)
        if int(len(data_count) / 7) > len(data_count) / 7:
            page_num = int(len(data_count) / 7)
        else:
            page_num = int(len(data_count) / 7)
        user = session.get('admin_user')
        return render_template('admin/admin_user_manage.html', data=data, page=page, page_num=page_num, user=user)
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/admin_edit_user', methods=['POST'])
def admin_edit_user_profile():
    if session.get('admin_user'):
        user_id = request.form.get('user_id')
        user_account = request.form.get('bj_user_account')
        user_name = request.form.get('bj_user_name')
        reg_date = request.form.get('bj_reg_date')
        print(user_account, user_name, reg_date)
        sql = f"UPDATE users_data SET users_data.user_name='{user_name}' WHERE users_data.user_id={user_id}"
        print(sql)
        SqlCx(sql)
        return redirect(url_for('admin.admin_user_manage_profile'))
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/delete_user', methods=['POST'])
def delete_user_profile():
    if session.get('admin_user'):
        if request.method == 'POST':
            user_id = request.form.get('user_id')
            print(user_id)
            sql = f"delete FROM users_data where user_id={user_id}"
            SqlCx(sql)
            return redirect(url_for("admin.admin_user_manage_profile"))
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/class_manage', methods=['GET'])
@admin_bp.route('/class_manage/<int:page>', methods=['GET'])
def admin_class_manage_profile(page=1):
    if session.get('admin_user'):
        a = (page - 1) * 7
        b = (page) * 7
        sql = f"select * from info_class limit {a},7"
        data = SqlCx(sql)
        print(data)
        sql = f"select * from info_class"
        data_count = SqlCx(sql)
        print(data)
        if int(len(data_count) / 7) > len(data_count) / 7:
            page_num = int(len(data_count) / 7)
        else:
            page_num = int(len(data_count) / 7)
        user = session.get('admin_user')
        return render_template('admin/admin_class_manage.html', data=data, page=page, page_num=page_num, user=user)
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/admin_add_class', methods=['POST'])
def admin_add_class_profile():
    if session.get('admin_user'):
        info_class_name = request.form.get('info_class_name')
        info_class_image = request.files.get('info_class_image')
        info_class_value = request.form.get('info_class_value')
        path = 'static/images/'
        now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        random_num = random.randint(0, 100)
        if random_num <= 10:
            random_num = str(0) + str(random_num)
        unique_name = str(now_time) + str(random_num)
        ext = str(info_class_image.filename).split('.', 1)[1]
        file_path = path + unique_name + '.' + ext
        info_class_image.save(file_path)
        info_class_image = '../' + file_path
        sql = f"INSERT INTO info_class values (null, '{info_class_name}', '{info_class_value}', '{info_class_image}')"
        print(sql)
        SqlCx(sql)
        return redirect(url_for('admin.admin_class_manage_profile'))
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/delete_class', methods=['POST'])
def delete_class_profile():
    if session.get('admin_user'):
        if request.method == 'POST':
            class_id = request.form.get('class_id')
            print(class_id)
            sql = f"delete FROM info_class where id={class_id}"
            SqlCx(sql)
            return redirect(url_for("admin.admin_class_manage_profile"))
        return True
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/admin_edit_class', methods=['POST'])
def admin_edit_class_profile():
    if session.get('admin_user'):
        if request.method == 'POST':
            info_class_name = request.form.get('info_class_name')
            info_class_value = request.form.get('info_class_value')
            info_class_image = request.files.get('info_class_image')
            info_class_id = request.form.get('info_class_id')
            print(info_class_id, info_class_name, info_class_value, info_class_image)
            if 'application/octet-stream' not in str(info_class_image):
                path = 'static/images/'
                now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                random_num = random.randint(0, 100)
                if random_num <= 10:
                    random_num = str(0) + str(random_num)
                unique_name = str(now_time) + str(random_num)
                ext = str(info_class_image.filename).split('.', 1)[1]
                file_path = path + unique_name + '.' + ext
                info_class_image.save(file_path)
                info_class_image = '../' + file_path
                sql = f"UPDATE info_class SET info_class_name='{info_class_name}', info_class_value='{info_class_value}', info_class_image='{info_class_image}' where id={info_class_id}"
                print(sql)
                SqlCx(sql)
            else:
                sql = f"UPDATE info_class SET info_class_name='{info_class_name}', info_class_value='{info_class_value}' where id={info_class_id}"
                print(sql)
                SqlCx(sql)
            return redirect(url_for('admin.admin_class_manage_profile'))
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/system_data', methods=['GET'])
def admin_system_manage_profile():
    if session.get('admin_user'):
        sql = f"SELECT * FROM info_comment,info_data,info_class WHERE info_data.info_class=info_class.info_class_value and info_comment.info_id=info_data.info_id GROUP BY info_comment.info_id ORDER BY info_data.info_date DESC LIMIT 5"
        data = SqlCx(sql)
        print(data)
        sql = f"SELECT info_class.info_class_name, COUNT(info_id) AS info_count, info_class.`*` FROM info_data, info_class WHERE info_data.info_class=info_class.info_class_value GROUP BY info_data.info_class ORDER BY info_count desc limit 5"
        info_class_data = SqlCx(sql)
        user = session.get('admin_user')
        path = os.getcwd()
        print(path)
        try:
            os.remove(path + r'\templates\admin\1.html')
            os.remove(path + r'\templates\admin\2.html')
        except:
            print('删除失败')
        dw.info_count()
        dw.user_count()
        return render_template('admin/admin_system_data.html', data=data, info_class_data=info_class_data, user=user)
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/admin_logout', methods=['GET'])
def admin_logout_profile():
    if session.get('admin_user'):
        session.pop('admin_user')
        return render_template('admin/admin_login.html')
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/data/<int:name>', methods=['GET'])
def admin_system_data_profile(name):
    dw.info_count()
    dw.user_count()
    return render_template(f'admin/{name}.html')


@admin_bp.route('/auth_manage', methods=['GET'])
def auth_manage_profile(page=1):
    if session.get('admin_user'):
        a = (page - 1) * 7
        sql1 = f"select * from admin_data where role=0 limit {a},7"
        data = SqlCx(sql1)
        info_data_list = []
        for i in data:
            info_data_dict = {}
            info_data_dict['id'] = i['id']
            info_data_dict['username'] = i['username']
            info_data_dict['password'] = i['password']
            info_data_dict['date'] = i['date']
            sql2 = f"SELECT COUNT(examine_data.id) AS exam_count from admin_data,examine_data where admin_data.username=examine_data.auth_id AND admin_data.role=0 AND admin_data.id={i['id']}"
            count = SqlCx(sql2)
            info_data_dict['exam_count'] = count[0]['exam_count']
            info_data_list.append(info_data_dict)
        print(info_data_list)

        # sql = f"SELECT admin_data.`*`, COUNT(examine_data.id) AS exam_count from admin_data,examine_data where admin_data.username=examine_data.auth_id AND admin_data.role=0 limit {a},7"
        # data = SqlCx(sql)
        # print(data)
        sql = f"select * from admin_data"
        data_count = SqlCx(sql)
        print(data)
        if int(len(data_count) / 7) > len(data_count) / 7:
            page_num = int(len(data_count) / 7)
        else:
            page_num = int(len(data_count) / 7)
        user = session.get('admin_user')
        return render_template('admin/admin_auth_manage.html', data=info_data_list, page=page, page_num=page_num,
                               user=user)
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/admin_add_auth', methods=['POST'])
def admin_add_auth_profile():
    if session.get('admin_user'):
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            print(username, password)
            da = datetime.datetime.now()
            sql = f"insert into admin_data values (null, '{username}', '{password}', 0, '{da}')"
            SqlCx(sql)
            return redirect(url_for('admin.auth_manage_profile'))
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/admin_edit_auth', methods=['POST'])
def admin_edit_auth_profile():
    """
    auth_id: 4
    username: auth3
    password: auth3
    :return:
    """
    if session.get('admin_user'):
        if request.method == 'POST':
            auth_id = request.form.get('auth_id')
            username = request.form.get('username')
            password = request.form.get('password')
            sql = f"update admin_data set username='{username}', password='{password}' where id={auth_id}"
            SqlCx(sql)
            return redirect(url_for('admin.auth_manage_profile'))
    else:
        return render_template('admin/admin_login.html')


@admin_bp.route('/delete_auth', methods=['POST'])
def admin_delete_auth_profile():
    """
    auth_id: 4
    :return:
    """
    if session.get('admin_user'):
        if request.method == 'POST':
            auth_id = request.form.get('auth_id')
            print(auth_id)
            sql = f"delete FROM admin_data where id={auth_id}"
            SqlCx(sql)
            return redirect(url_for('admin.auth_manage_profile'))
    else:
        return render_template('admin/admin_login.html')
