# coding:utf-8
import datetime
import random

from flask import render_template, request, jsonify, session, redirect, url_for, flash

from sql_cx import SqlCx
from . import class_bp


# 分类页视图函数
@class_bp.route('/index_class', methods=["GET"])
def index_class_profile():
    sql = f"select * from info_class"
    class_data = SqlCx(sql)
    return render_template("class.html", class_data=class_data)


@class_bp.route('/info_class/<int:info_class>', methods=["GET"])
def info_class_profile(info_class):
    sql = f"SELECT * FROM help_system.info_data, users_data where info_class={info_class} and info_data.info_user_id=users_data.user_account order by info_data.info_date desc"
    data = SqlCx(sql)
    print(data)
    sql = f"select * from info_class where info_class_value={info_class}"
    info_class_data = SqlCx(sql)
    return render_template("info_class.html", info_data=data, info_class=info_class_data[0])


@class_bp.route('/info_class/<string:info_class>', methods=["GET"])
def info_class_examine_profile(info_class):
    return redirect(url_for('index_class.info_examine_profile'))


@class_bp.route('/api/info_class/<int:info_class>/<int:page>', methods=["GET"])
def index_profile_ajax(info_class, page=1):
    print(info_class)
    a = (page - 1) * 7
    sql = f"SELECT * FROM info_data, users_data, info_class where info_data.info_user_id=users_data.user_account and info_data.info_class=info_class.info_class_value and info_data.info_class='{info_class}' and info_data.info_examine=1 order by info_data.info_date desc limit {a}, 7"
    info_data = SqlCx(sql)
    print(len(info_data))
    print(info_data)
    info_data_list = []
    for data in info_data:
        info_data_dict = {}
        info_data_dict['user_name'] = data['user_name']
        info_data_dict['user_head_image'] = data['user_head_image']
        info_data_dict['info_date'] = str(data['info_date'])
        info_data_dict['info_state'] = data['info_state']
        info_data_dict['info_id'] = data['info_id']
        info_data_dict['info_image'] = data['info_image']
        info_data_dict['info_title'] = data['info_title']
        info_data_dict['info_content'] = data['info_content']
        info_data_dict['info_class_name'] = data['info_class_name']
        info_data_list.append(info_data_dict)
    print(info_data_list)
    return jsonify(info_data_list)


@class_bp.route('/search', methods=['GET'])
def index_search_profile():
    if request.method == 'GET':
        word = request.args.get('word')
        print(word)
        sql = f"select * from info_data,info_class,users_data WHERE info_data.info_class=info_class.info_class_value AND info_data.info_user_id=users_data.user_account AND info_title LIKE '%{word}%'  and info_data.info_examine=1"
        print(sql)
        data = SqlCx(sql)
        print(data)
        return render_template('info_search.html', info_data=data, word=word)


@class_bp.route('/api/search/<string:word>/<int:page>', methods=["GET"])
def search_profile_ajax(word, page=1):
    print(word)
    a = (page - 1) * 7
    sql = f"select * from info_data,info_class,users_data WHERE info_data.info_class=info_class.info_class_value AND info_data.info_user_id=users_data.user_account AND info_title LIKE '%{word}%'  and info_data.info_examine=1 limit {a}, 7"
    info_data = SqlCx(sql)
    print(len(info_data))
    print(info_data)
    info_data_list = []
    for data in info_data:
        info_data_dict = {}
        info_data_dict['user_name'] = data['user_name']
        info_data_dict['user_head_image'] = data['user_head_image']
        info_data_dict['info_date'] = str(data['info_date'])
        info_data_dict['info_state'] = data['info_state']
        info_data_dict['info_id'] = data['info_id']
        info_data_dict['info_image'] = data['info_image']
        info_data_dict['info_title'] = data['info_title']
        info_data_dict['info_content'] = data['info_content']
        info_data_dict['info_class_name'] = data['info_class_name']
        info_data_list.append(info_data_dict)
    print(info_data_list)
    return jsonify(info_data_list)

@class_bp.route('/info_examine', methods=['GET'])
def info_examine_profile():
    examine_user = session.get('examine_user')
    if examine_user:
        return render_template('examine/examine_index.html', examine_user=examine_user)
    else:
        code = 3230
        return render_template('examine/examine_login.html', code=code)


@class_bp.route('/info_examine_login', methods=['POST'])
def info_examine_login_profile():
    if request.method == 'GET':
        code = 3128
        return render_template('examine/examine_login.html', code=code)
    elif request.method == 'POST':
        user_input_dict = request.form.to_dict()
        print(user_input_dict)
        if user_input_dict:
            sql = f"SELECT * FROM help_system.admin_data where username='{user_input_dict['username']}' and password='{user_input_dict['password']}' and role=0"
            user_data = SqlCx(sql)
            print('user_data', user_data)
            yzm = user_input_dict['yzm']
            yzm_code = user_input_dict['code']
            if yzm != yzm_code:
                flash('验证码错误')
                return render_template('login.html')
            if user_data:
                session['examine_user'] = user_input_dict['username']
                return redirect(url_for('index_class.info_examine_profile'))
            else:
                flash('账户名或密码错误')
                code = 1238
                return render_template('examine/examine_login.html', code=code)
            return 'alert("登录成功")'


@class_bp.route('/examine_detail', methods=['GET'])
def examine_detail_profile():
    examine_user = session.get('examine_user')
    if examine_user:
        sql = f"select * from info_data, info_class where info_data.info_class=info_class.info_class_value and info_data.info_examine=0"
        info_data = SqlCx(sql)
        print(len(info_data))
        if len(info_data) > 1:
            info_data = random.choice(info_data)
            sql = f"select * from users_data where user_account='{info_data['info_user_id']}'"
            user_data = SqlCx(sql)
            return render_template('examine/examine_detail.html', info=info_data, user=user_data[0], examine_user=examine_user)
        else:
            return render_template('examine/examine_finish.html', examine_user=examine_user)
    else:
        code = 3230
        return render_template('examine/examine_login.html', code=code)

@class_bp.route('/examine_logout', methods=['GET'])
def examine_logout_profile():
    examine_user = session.get('examine_user')
    if examine_user:
        session.pop('examine_user')
        code = 1110
        flash('您已退出审核员账号！')
        return render_template('examine/examine_login.html', code=code)
    else:
        code = 1110
        return render_template('examine/examine_login.html', code=code)


@class_bp.route('/examine_no/<int:info_id>', methods=['GET'])
def examine_no_profile(info_id):
    examine_user = session.get('examine_user')
    if examine_user:
        info_sql = f"UPDATE info_data SET info_examine=2 WHERE info_id={info_id}"
        SqlCx(info_sql)
        da = datetime.datetime.now()
        examine_sql = f"INSERT INTO examine_data VALUES (null, '{info_id}', '{examine_user}', '{da}', 2, '无');"
        SqlCx(examine_sql)
        return redirect(url_for('index_class.examine_detail_profile'))
    else:
        code = 3230
        return render_template('examine/examine_login.html', code=code)


@class_bp.route('/examine_yes/<int:info_id>', methods=['GET'])
def examine_yes_profile(info_id):
    examine_user = session.get('examine_user')
    if examine_user:
        info_sql = f"UPDATE info_data SET info_examine=1 WHERE info_id={info_id}"
        SqlCx(info_sql)
        da = datetime.datetime.now()
        examine_sql = f"INSERT INTO examine_data VALUES (null, '{info_id}', '{examine_user}', '{da}', 1, '无');"
        SqlCx(examine_sql)
        return redirect(url_for('index_class.examine_detail_profile'))
    else:
        code = 3230
        return render_template('examine/examine_login.html', code=code)
