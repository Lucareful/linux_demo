import socket
import threading

from applications import app


class WebServer(object):

    def __init__(self):
        # 创建套接字
        tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置地址可以复用
        tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口和IP
        tcp_server.bind(("", 43999))
        # 开启监听，最大监听数
        tcp_server.listen(128)
        # 定义实例属性，保存套接字对象
        self.tcp_server = tcp_server

    def start(self):
        while True:
            new_client_socket, ip_port = self.tcp_server.accept()
            print("客户端{}连接".format(ip_port))
            # 创建线程对象
            # 调用功能处理函数处理请求并响应
            threads = threading.Thread(target=self.request_handler, args=(new_client_socket, ip_port))
            threads.setDaemon(True)
            threads.start()

    def request_handler(self, new_client_socket, ip_port):
        """接收消息并响应"""
        request_data = new_client_socket.recv(1024)

        # 判断协议是否为空
        if not request_data:
            print("客户端{}已退出连接...".format(ip_port))
            new_client_socket.close()
            return

        responses = app.application(request_data, ip_port)
        # 发送响应的报文
        new_client_socket.send(responses)

        # 关闭当前连接
        new_client_socket.close()


if __name__ == '__main__':
    # 创建WebServer对象
    ws = WebServer()
    ws.start()
