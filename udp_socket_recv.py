#! /usr/bin/python3

import socket

addr = ("127.0.0.1", 9999)

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind(addr)

recv_data, ip_port = udp_socket.recvfrom(1024)

print(recv_data.decode())
print(ip_port)

udp_socket.close()