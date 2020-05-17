#! /usr/bin/python3
import socket

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ("127.0.0.1", 4399)
tcp_client.connect(addr)

# 循环发送消息
while True:
    data = input()
    if len(data) != 0:
        tcp_client.send(data.encode(errors="ignore"))
    else:
        tcp_client.close()
        break
