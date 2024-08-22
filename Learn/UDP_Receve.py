# DUP接收方 类似于服务器
from socket import socket, AF_INET, SOCK_DGRAM

# 1.创建socket对象
recv_socket = socket(AF_INET, SOCK_DGRAM)

# 2.绑定IP和端口号
ip_port = ('127.0.0.1', 8888)
recv_socket.bind(ip_port)

# 3.接收发送方的数据
recv_data, recv_addr = recv_socket.recvfrom(1024)
print('接收到的数据为:', recv_data.decode('utf-8'))

# 4.准备回复发送方的数据
data = input('输入回复发送方的数据:')

# 5.通过地址回复发送方
recv_socket.sendto(data.encode('utf-8'), recv_addr)

# 6.关闭接收方
recv_socket.close()




