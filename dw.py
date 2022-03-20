# coding: utf-8
import datetime
import os
from pyecharts import options as opts
from pyecharts.charts import Bar

from sql_cx import SqlCx


def info_count():
    sql = f"select info_date from info_data order by info_date asc"
    data = SqlCx(sql)
    # 折线图 分类 统计
    detail_date_list = []
    data_dict = {}
    for i in data:
        a = i['info_date']
        b = datetime.datetime.strftime(a, '%y-%m-%d')
        # print(b)
        detail_date_list.append(str(b))
    for key in detail_date_list:
        data_dict[key] = data_dict.get(key, 0) + 1
    print(data_dict)
    bar = Bar()
    # 指定柱状图的横坐标
    bar.add_xaxis(list(data_dict.keys()))
    # 指定柱状图的纵坐标，而且可以指定多个纵坐标
    bar.add_yaxis("数量统计", list(data_dict.values()))
    # 指定柱状图的标题
    bar.set_global_opts(title_opts=opts.TitleOpts(title="发帖数量统计图"))
    # 参数指定生成的html名称
    path = 'templates/admin/1.html'
    bar.render(path)


def user_count():
    sql = f"select user_reg_date from users_data order by user_reg_date asc"
    data = SqlCx(sql)
    # print(data)
    # 折线图 分类 统计
    detail_date_list = []
    data_dict = {}
    for i in data:
        a = i['user_reg_date']
        b = datetime.datetime.strftime(a, '%y-%m-%d')
        detail_date_list.append(str(b))
    for key in detail_date_list:
        data_dict[key] = data_dict.get(key, 0) + 1
    print(data_dict)
    bar = Bar()
    # 指定柱状图的横坐标
    bar.add_xaxis(list(data_dict.keys()))
    # 指定柱状图的纵坐标，而且可以指定多个纵坐标
    bar.add_yaxis("数量统计", list(data_dict.values()))
    # 指定柱状图的标题
    bar.set_global_opts(title_opts=opts.TitleOpts(title="用户注册数量统计图"))
    # 参数指定生成的html名称
    path = 'templates/admin/2.html'
    # try:
    #     os.remove(path)
    # except:
    #     print()
    bar.render(path)
