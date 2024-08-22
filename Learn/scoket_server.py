# TCP服务器端代码
# 多次通信

from socket import socket, AF_INET, SOCK_STREAM

# AF_INET 用于inter之间的通信
# SOCK_STREAM 表示TCP之间的通信


# 1.创建socket对象
server_socket = socket(AF_INET, SOCK_STREAM)

# 2.绑定IP地址和端口
ip = '127.0.0.1'
port = 8888
server_socket.bind((ip, port))

# 3.监听
server_socket.listen(5)
print('服务器正常启动')

# 4.等待客户端连接
# client_socket表示服务器和客户端之间的套接字对象
# server_socket继续监听别的请求
client_socket, client_addr = server_socket.accept()  # 系列解包赋值
print(f'客户端{client_addr}连接成功')

# 5.接受来自客户端数据
# 多次通信
# info来自客户端的数据
info = client_socket.recv(1024).decode('utf-8')
# bye定义是是否为中止通信的表示
while info != 'bye':
    if info != '':
        print('接受到数据为:', info)

    # 接受到了来自客户端的信息,现在要向客户端回复数据
    data = input('向客户端回复的数据是:')

    # 服务器端回复客户端
    client_socket.send(data.encode('utf-8'))

    # 判断是否为结束语bye,是则终止通信
    if data == 'bye':
        break

    # 再次从客户端接受到数据
    info = client_socket.recv(1024).decode('utf-8')

# 6.关闭服务器端
# 先关闭客户端连接的套接字
# 再关闭监听的套接字 表示服务器不再接受新的客户端连接
client_socket.close()
server_socket.close()
print('服务器关闭')