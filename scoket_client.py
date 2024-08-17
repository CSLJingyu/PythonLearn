# TCP客户端代码

from socket import  socket, AF_INET, SOCK_STREAM

# 1.创建socket对象
client_socket = socket.socket()

# 2.连接IP地址和端口
ip = '127.0.0.1'
port = 8888
client_socket.connct((ip, port))
print('-----和服务器连接成功-----')

# 3.客户端发送数据
client_socket.send('hello python'.encode('utf-8'))

# 4.关闭客户端
client_socket.close()
print('发送结束')