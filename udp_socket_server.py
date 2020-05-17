#! /usr/bin/python3
import socket

# 使用ipv4 udp连接
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 使用ipv4 tcp连接

addr = ("127.0.0.1", 8888)
# tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

udp_socket.sendto("Luenci".encode(), addr)

# 关闭套接字
udp_socket.close()
# udp_socket.close()