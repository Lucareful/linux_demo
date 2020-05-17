#! /usr/bin/python3

import socket
import threading

def send_message(content, addr):
    """
    :param addr:发送的信息主机的地址（ip和端口）
    :return:None
    """
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(content.encode(), addr)
    udp_socket.close()


def recev_message(addr):
    """
    :param addr: 接收信息的主机地址
    :return: 
    """
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(addr)
    data, _ = udp_socket.recvfrom(1024)
    udp_socket.close()

    return data.decode()


if __name__ == '__main__':

    str = "\n\n--------------   菜单   --------------\n"
    str += "-------------1.发送信息---------------\n"
    str += "-------------2.接收信息---------------\n"
    str += "-------------3.退出程序---------------\n"

    while True:
        print(str)
        flag = int(input("请输入您要选择的功能:(如：1)\n"))
        if flag == 1:
            try:
                ip = input("请输入您发送主机的ip：(回车键结束)\n")
                port = int(input("请输入您发送主机的port：(回车键结束)\n"))
                content = input("请输入您发送信息内容：(回车键结束)\n")
                addr = (ip, port)
                send_message(content=content, addr=addr)
                print("发送信息成功")
            except BaseException as e:
                print("发送信息失败：原因为", e)

        elif flag == 2:
            try:
                ip = input("请输入您接收主机的ip：(回车键结束)\n")
                port = int(input("请输入您接收主机的port：(回车键结束)\n"))
                addr = (ip, port)
                data = recev_message(addr)
                print("您接收的信息为:", data)
            except BaseException as e:
                print("接收信息失败：原因为", e)
        else:
            print("程序已退出...")
            break

