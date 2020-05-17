#! /usr/bin/python3
import socket

# 创建套接字
tcp_serve = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置地址可以复用
tcp_serve.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 绑定端口和IP
tcp_serve.bind(("", 43999))
# 开启监听，最大监听数
tcp_serve.listen(128)

while True:
    # 等待客户端连接,程序会进入阻塞状态（等待客户端连接），如果由客户端连接后，程序会自动解除阻塞状态
    # 收发数据
    print("开始接收信息")
    new_client, ip_port = tcp_serve.accept()
    while True:
        recv_data = new_client.recv(1024)
        if len(recv_data) != 0:
            recv_text = recv_data.decode()
            print("接收来自{}的消息:{}".format(ip_port, recv_text))
        else:
        # 关闭连接
            new_client.close()
            print("客户端{}退出".format(ip_port))
            break

tcp_serve.close()
