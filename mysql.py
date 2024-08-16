# 导入操作包
# 如果不想手动commit确认,可以构建连接对象的时候,设置自动commit的属性
# 查询后,使用游标对象.fetchall()可以得到全部的查询结果封装在嵌套元组内
# 使用游标对象.execute(sql语句)执行sql语句

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
# cursor.execute("CREATE TABLE tb_user(id INT, name VARCHAR(8), age int)")
# 修改列属性
# cursor.execute('ALTER TABLE tb_user MODIFY COLUMN id INT AUTO_INCREMENT PRIMARY KEY;')
# 执行插入语句
# cursor.execute("Insert into tb_user value(3, 'kk', 32)")
# 确认插入行为,执行sql语句
# 如果在获取连接对象的时设置自动提交就可以不用再写
conn.commit()

# 使用游标对象,执行sql语句
cursor.execute("SELECT * FROM tb_user")

# 获取查询结果
# results: tuple = cursor.fetchall()
# for result in results:
#     print(result)


# 修改结果
# cursor.execute("update tb_user set name='llff' where id=1")
# conn.commit()


# 删除sql
cursor.execute("delete from tb_user where id = 3")
conn.commit()
# 关闭到连接数据库的连接
conn.close()