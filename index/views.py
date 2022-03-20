# coding:utf-8
from flask import render_template, jsonify

from index import index_bp
from sql_cx import SqlCx


# 首页视图函数
@index_bp.route('/', methods=["GET"])
@index_bp.route('/index', methods=["GET"])
def index_profile():
    # info_data = app.InfoData.query.limit(30).all()
    return render_template("index.html")


@index_bp.route('/api/index/<int:page>', methods=["GET"])
def index_profile_ajax(page=1):
    print(page)
    a = (page - 1) * 7
    sql = f"SELECT * FROM info_data, users_data, info_class where info_data.info_user_id=users_data.user_account and info_data.info_class=info_class.info_class_value and info_data.info_examine=1 order by info_data.info_date desc limit {a}, 7"
    info_data = SqlCx(sql)
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
    return jsonify(info_data_list)
