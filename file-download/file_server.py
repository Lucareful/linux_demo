import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置套接字地址可重用
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

addr = ("127.0.0.1", 4399)

tcp_socket.bind(addr)
tcp_socket.listen(128)

while True:
    tcp_request, ip_port = tcp_socket.accept()
    print("客户端加入")
    file_name = tcp_request.recv(1024).decode()

    # 根据文件名读取文件内容
    try:
        with open("../"+file_name, "rb") as file:
            # 把读取的文件内容发送给客户端
            while True:
                file_data = file.read(1024)
                if file_data:
                # 发送文件
                    tcp_request.send(file_data)
                else:
                    print("读取完毕！已发送")
                    break
    except Exception as e:
        tcp_request.send("404".encode())
        print("文件下载失败,错误为：{}".format(e))
    tcp_request.close()

tcp_socket.close()