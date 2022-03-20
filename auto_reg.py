# coding: utf-8
from sql_cx import SqlCx

f = open('name.txt', 'r', encoding='utf-8').readlines()
print(f)

for i in range(60):
    name = f[i].replace('\n', '')
    print(name)
    sql = f"INSERT INTO users_data(`user_id`, `user_account`, `user_password`, `user_name`, `user_head_image`)" \
          f" VALUES (null , '{i + 10000}', '{i + 10000}', '{name}', '../static/images/index_user.png');"
    SqlCx(sql)
