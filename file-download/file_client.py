import socket

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ("127.0.0.1", 4399)
tcp_client.connect(addr)

file_name = input("请输入要下载的文件名:\n")
tcp_client.send(file_name.encode())

# 创建文件接收内容并保存
with open(file_name, "w") as file:
    while True:
        data = tcp_client.recv(1024).decode()
        if data != "404":
            file.write(data)
        elif data == "404":
            print("文件下载失败")
            break
        else:
            break

tcp_client.close()
