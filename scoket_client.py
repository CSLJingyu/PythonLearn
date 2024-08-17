import socket

# 1.创建socket对象
client_socket = socket.socket()

# 2.连接IP地址和端口
ip = '127.0.0.1'
port = 8888
client_socket.connect((ip, port))
print('-----和服务器连接成功-----')

# 3.客户端发送数据
# client_socket.send('hello python'.encode('utf-8'))
# 多次通信
info=''
while info != 'bye':
    # 准备向服务器端发送数据
    send_data = input('向服务器端发送数据是:')
    client_socket.send(send_data.encode('utf-8'))

    # 判断是否为bye
    if send_data == 'bye':
        break

    # 如果不是bye,会接收来自服务器端发回的数据info
    info = client_socket.recv(1024).decode('utf-8')
    print('收到来自服务器端的数据:', info)

# 4.关闭客户端
client_socket.close()