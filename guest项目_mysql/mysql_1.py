import time
from pymysql import cursors, connect
"""
connect():建立数据库连接
cursor():获取数据库操作游标
execute():执行SQL语句
commit(): 提交数据库执行
close():关闭数据库连接
"""
# 连接数据库
conn = connect(host="127.0.0.1",
               user="root",
               password="root",
               db="guest",
               charset="utf8",
               cursorclass=cursors.DictCursor)
try:
    with conn.cursor() as cursors:
        # sign_guest添加数据
        mysqls ="INSERT INTO sign_event (name_1, limit_1, status_1, address, start_time, create_time) VALUES('奔驰发布会', 4, True,'孝感', '2019-5-20 20:00:00',NOW());"
        cursors.execute(mysqls)
    conn.commit()

    # with conn.cursor() as cursors:
    #     # 创建嘉宾数据库
    #     sql ="INSERT INTO sign_guest (realname, phone, email, sign, event_id, create_time) VALUES('德玛', 18888888880,'jieke@mail.com', 0,1,NOW());"
    #     cursors.execute(sql)
    # conn.commit()


    # with conn.cursor() as cursors:
    #     # 查询嘉宾数据
    #     sql = "SELECT realname, phone, email, sign FROM sign_guest WHERE phone=%s"
    #     cursors.execute(sql, ('18888888888',))
    #     result = cursors.fetchone()
    #     print(result)
finally:
    conn.close()