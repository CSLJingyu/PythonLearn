# 导入操作包
from pymysql import Connection

# 获取连接到mysql数据库的操作对象
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456'
)

# 输出mysql的版本信息
# print(conn.get_server_info())

'''
执行非查询性质sql语句
'''
# 获取游标对象(用于操作数据库)
cursor = conn.cursor()
# 选择操作的数据库
conn.select_db("db1")
# 使用游标对象,执行建表sql语句
cursor.execute("CREATE TABLE tb_user(id INT, name VARCHAR(8), age int)")

# 关闭到连接数据库的连接
conn.close()