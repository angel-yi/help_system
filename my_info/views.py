# coding:utf-8
import datetime
import random
from flask import render_template
from flask import session, url_for, redirect, request, flash

from sql_cx import SqlCx
from . import my_info_bp


# 个人首页
@my_info_bp.route('/my_info', methods=["GET"])
def my_info_profile():
    if session.get('user'):
        print(session.get('user'))
        user_account = session.get('user')
        sql = f"SELECT * FROM help_system.users_data where user_account = '{user_account}';"
        data = SqlCx(sql)
        data = data[0]
        data['user_reg_date'] = data['user_reg_date'].strftime('%Y-%m-%d')
        return render_template("my_info.html", data=data)
    else:
        return redirect(url_for('my_info.login_profile'))


@my_info_bp.route('/login', methods=['GET', 'POST'])
def login_profile():
    if request.method == 'GET':
        code = 3128
        return render_template('login.html', code=code)
    elif request.method == 'POST':
        user_input_dict = request.form.to_dict()
        print(user_input_dict)
        if user_input_dict:
            # newobj = User(username=p_user, email=p_email, password=p_password)
            # user_data = app.UserData(user_name=user_input_dict['username'], user_password=user_input_dict['password'])
            # app.help_database.session.filter(user_data)
            # app.help_database.session.commit()
            # user_data = app.UserData.query.fiter_by(user_name=user_input_dict['username'], user_password=user_input_dict['password']).first()
            sql = f"SELECT * FROM help_system.users_data where user_account='{user_input_dict['username']}' and user_password='{user_input_dict['password']}';"
            user_data = SqlCx(sql)
            print('user_data', user_data)
            yzm = user_input_dict['yzm']
            yzm_code = user_input_dict['code']
            if yzm != yzm_code:
                flash('验证码错误')
                return render_template('login.html')
            if user_data:
                session['user'] = user_input_dict['username']
                return redirect(url_for('my_info.my_info_profile'))
            else:
                flash('账户名或密码错误')
                code = 1238
                return render_template('login.html', code=code)
            return 'alert("登录成功")'


@my_info_bp.route('/register', methods=['GET', 'POST'])
def register_profile():
    if request.method == 'GET':
        code = 3069
        return render_template('register.html', code=code)
    elif request.method == 'POST':
        reg_form = request.form.to_dict()
        print(reg_form)
        if reg_form:
            pwd1 = reg_form['password1']
            pwd2 = reg_form['password2']
            user_account = reg_form['useraccount']
            username = reg_form['username']
            yzm = reg_form['yzm']
            yzm_code = reg_form['code']
            sql = f"SELECT * FROM help_system.users_data where user_account = '{user_account}';"
            data = SqlCx(sql)
            if yzm != yzm_code:
                flash('验证码错误')
                return render_template('register.html')
            if len(user_account) < 6:
                flash('账号最短为6个字符')
                return render_template('register.html')
            if len(username) > 16:
                flash('昵称最多不超过8个汉字')
                return render_template('register.html')
            if len(pwd1) < 6:
                flash('密码最短为6个字符')
                return render_template('register.html')
            if data:
                flash('账号已经存在，请更换')
                code = 2255
                return render_template('register.html', code=code)
            if pwd1 != pwd2:
                flash('两次密码不一致')
                code = 2255
                return render_template('register.html', code=code)
            else:
                sql = f"INSERT INTO users_data(`user_id`, `user_account`, `user_password`, `user_name`, `user_head_image`) VALUES (null , '{user_account}', '{pwd2}', '{username}', '../static/images/index_user.png');"
                SqlCx(sql)
                code = 1156
                flash('注册成功，请登录!')
                return render_template('login.html', code=code)
        return reg_form


@my_info_bp.route('/logout', methods=['GET'])
def logout_profile():
    if request.method == 'GET':
        code = '2356'
        try:
            session.pop('user')
        except:
            return render_template('login.html', code=code)
        flash('您已经退出登录')
        return render_template('login.html', code=code)


@my_info_bp.route('/my_info_data', methods=['GET'])
def my_info_data_profile():
    if session.get('user'):
        print(session.get('user'))
        user_account = session.get('user')
        sql = f"SELECT * FROM help_system.info_data, users_data, info_class where info_class.info_class_value=info_data.info_class and info_data.info_user_id='{user_account}' and info_data.info_user_id=users_data.user_account order by info_data.info_date desc"
        data = SqlCx(sql)
        return render_template("my_info_data.html", info_data=data)
    else:
        return redirect(url_for('my_info.login_profile'))


@my_info_bp.route('/my_like', methods=['GET'])
def my_like_profile():
    if session.get('user'):
        print(session.get('user'))
        user_account = session.get('user')
        sql = f"SELECT * FROM users_data, users_like, info_data, info_class where info_class.info_class_value=info_data.info_class and users_like.user_id='{user_account}' AND users_data.user_account=info_data.info_user_id  AND users_like.info_id=info_data.info_id  order by users_like.date desc "
        data = SqlCx(sql)
        print(data)
        return render_template("my_like.html", info_data=data)
    else:
        return redirect(url_for('my_info.login_profile'))


@my_info_bp.route('/my_comment', methods=['GET'])
def my_comment_profile():
    if session.get('user'):
        print(session.get('user'))
        user_account = session.get('user')
        sql = f"SELECT *,info_comment.id AS comment_id FROM users_data, info_comment, info_data, info_class where info_class.info_class_value=info_data.info_class and info_comment.user_id='{user_account}' AND users_data.user_account=info_data.info_user_id  AND info_comment.info_id=info_data.info_id  order by info_comment.comment_date desc "
        data = SqlCx(sql)
        print(data)
        return render_template("my_comment.html", info_data=data)
    else:
        return redirect(url_for('my_info.login_profile'))


@my_info_bp.route('/my_count', methods=['GET'])
def my_count_profile():
    if session.get('user'):
        print(session.get('user'))
        user_account = session.get('user')
        sql = f"SELECT * FROM users_data where user_account='{user_account}'"
        print(sql)
        data = SqlCx(sql)
        print(data)
        sql = f"SELECT COUNT(info_data.info_id) AS info_count FROM info_data WHERE info_data.info_user_id='{user_account}'"
        info_count = SqlCx(sql)
        sql = f"SELECT COUNT(info_comment.id) AS comment_count FROM info_comment WHERE info_comment.user_id='{user_account}'"
        comment_count = SqlCx(sql)
        sql = f"SELECT COUNT(users_like.id) AS like_count FROM users_like WHERE users_like.user_id='{user_account}'"
        like_count = SqlCx(sql)
        return render_template("my_count.html", info_data=data[0], info_count=info_count[0],
                               comment_count=comment_count[0], like_count=like_count[0])
    else:
        return redirect(url_for('my_info.my_like_profile'))


@my_info_bp.route('/delete_like/<int:users_like_id>', methods=['GET'])
def delete_like_profile(users_like_id):
    user_id = session.get('user')
    if user_id:
        # 返回发布页面
        sql = f"delete FROM users_like where id={users_like_id}"
        data = SqlCx(sql)
        print(data)
        return redirect(url_for('my_info.my_like'))
    else:
        flash('请您先登录！')
        return redirect(url_for('my_info.login_profile'))


@my_info_bp.route('/delete_comment/<int:comment_id>', methods=['GET'])
def delete_comment_profile(comment_id):
    user_id = session.get('user')
    if user_id:
        # 返回发布页面
        sql = f"delete FROM info_comment where id={comment_id}"
        data = SqlCx(sql)
        print(data)
        return redirect(url_for('my_info.my_comment'))
    else:
        flash('请您先登录！')
        return redirect(url_for('my_info.login_profile'))


@my_info_bp.route('/edit_head_image', methods=['GET', 'POST'])
def edit_head_image_profile():
    user_account = session.get('user')
    if user_account:
        # 返回发布页面
        if request.method == 'GET':
            sql = f"SELECT * FROM help_system.users_data where user_account = '{user_account}';"
            data = SqlCx(sql)
            return render_template("edit_head_image.html", data=data[0])
        elif request.method == 'POST':
            # 开始修改
            img = request.files.get('image')
            print(img)
            path = 'static/user_images/'
            now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            random_num = random.randint(0, 100)
            if random_num <= 10:
                random_num = str(0) + str(random_num)
            unique_name = str(now_time) + str(random_num)
            ext = str(img.filename).split('.', 1)[1]
            file_path = path + unique_name + '.' + ext
            img.save(file_path)
            user_id = session.get('user')
            info_image = '../' + file_path
            info_user_id = user_id
            sql = f"update users_data set user_head_image='{info_image}' where user_account='{info_user_id}'"
            print(sql)
            SqlCx(sql)
            return redirect(url_for('my_info.my_info_profile'))
    else:
        flash('请您先登录！')
        return redirect(url_for('my_info.login_profile'))


@my_info_bp.route('/edit_name', methods=['GET', 'POST'])
def edit_name_profile():
    user_account = session.get('user')
    if user_account:
        if request.method == 'GET':
            sql = f"SELECT * FROM help_system.users_data where user_account = '{user_account}';"
            data = SqlCx(sql)
            return render_template("edit_name.html", data=data[0])
        elif request.method == 'POST':
            user_name = request.form.get('user_name')
            pwd1 = request.form.get('pwd1')
            pwd2 = request.form.get('pwd2')
            tel = request.form.get('tel')
            if pwd1 != pwd2:
                flash('两次密码不一致')
                sql = f"SELECT * FROM help_system.users_data where user_account = '{user_account}';"
                data = SqlCx(sql)
                return render_template('edit_name.html', data=data[0])
            sql = f"update users_data set user_name='{user_name}', user_password='{pwd2}', user_tel='{tel}' where user_account='{user_account}'"
            print(sql)
            SqlCx(sql)
            return redirect(url_for('my_info.my_info_profile'))
    else:
        flash('请您先登录！')
        return redirect(url_for('my_info.login_profile'))
