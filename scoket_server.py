# TCP服务器端代码

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
client_socket, client_addr = server_socket.accept()  # 系列解包赋值

# 5.接受来自客户端数据
data = client_socket.recv(1024)
print('客户端发送过来的数据:', data.decode('utf-8'))  # 要求客户端发送过来的数据使用utf-8进行编码

# 6.关闭服务器端
client_socket.close()