# coding:utf-8
import pymysql
from datetime import timedelta

pymysql.install_as_MySQLdb()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from index import index_bp
from detail import detail_bp
from message import message_bp
from chat import chat_bp
from chat_send_message import chat_send_message_bp
from index_class import class_bp
from my_info import my_info_bp
from add_info import add_info_bp
from admin import admin_bp

app = Flask(__name__)
help_database = SQLAlchemy(app)


class DefaultConfig(object):
    """默认配置"""
    SECRET_KEY = 'TPmi4aLWRbyVq8zu9v82dWYW1'
    SQLALCHEMY_DATABASE_URI = 'mysql://angel_info_system:INFO_system@rm-m5e42302277dox30fno.mysql.rds.aliyuncs.com:3306/help_system'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)


class InfoData(help_database.Model):
    """
    信息表
    """
    __tablename__ = 'info_data'

    info_id = help_database.Column('info_id', help_database.Integer, primary_key=True, doc='主键ID')
    info_title = help_database.Column('info_title', help_database.String(100), doc='信息标题')
    info_content = help_database.Column('info_content', help_database.String(1000), doc='信息内容')
    info_image = help_database.Column('info_image', help_database.String(100), doc='信息图片')
    info_date = help_database.Column('info_date', help_database.DateTime, doc='发布时间')
    info_state = help_database.Column('info_state', help_database.Integer, doc='当前状态')
    info_user_id = help_database.Column('info_user_id', help_database.Integer,
                                        help_database.ForeignKey('users_data.user_id'), doc='发布者id')
    info_user_data = help_database.relationship('UserData')


class UserData(help_database.Model):
    """
    用户表
    """
    __tablename__ = 'users_data'

    user_id = help_database.Column('user_id', help_database.Integer, primary_key=True, doc='主键ID')
    user_name = help_database.Column('user_name', help_database.String(100), doc='昵称')
    user_password = help_database.Column('user_password', help_database.String(100), doc='密码')
    user_head_image = help_database.Column('user_head_image', help_database.String(100), doc='头像')
    user_reg_date = help_database.Column('user_reg_date', help_database.DateTime, doc='注册时间')
    info_info = help_database.relationship('InfoData')


class ChatData(help_database.Model):
    """
    聊天表
    """
    __tablename__ = 'chat_data'

    chat_id = help_database.Column('chat_id', help_database.Integer, primary_key=True, doc='主键ID')
    chat_hash = help_database.Column('chat_hash', help_database.String(50), doc='两个id的哈希值')
    chat_date = help_database.Column('chat_date', help_database.DateTime, doc='消息发送时间')
    chat_content = help_database.Column('chat_content', help_database.String(500), doc='消息内容')
    chat_state = help_database.Column('chat_state', help_database.Integer, doc='消息类型')


app.config.from_object(DefaultConfig)

# 将蓝图注册进来
app.register_blueprint(index_bp)
app.register_blueprint(detail_bp)
app.register_blueprint(message_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(chat_send_message_bp)
app.register_blueprint(class_bp)
app.register_blueprint(my_info_bp)
app.register_blueprint(add_info_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    app.run(debug=True)
