# DUP发送方 类似于客户端
from socket import socket, AF_INET, SOCK_DGRAM

# 1.创建socket对象
send_socket = socket(AF_INET, SOCK_DGRAM)

# 2.准备发送数据
data = input('输入发送数据:')

# 3.指定接收方的IP和端口
ip_port = ('127.0.0.1', 8888)

# 4.发送数据
send_socket.sendto(data.encode('utf-8'), ip_port)

# 接收来自接收方的数据
recv_data,addr = send_socket.recvfrom(1024)
print('接收到数据为:', recv_data.decode('utf-8'))

# 5.关闭socket对象
send_socket.close()