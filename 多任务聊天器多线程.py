#! /usr/bin/python3

import socket
import threading


def send_message():
    """
    :param addr:发送的信息主机的地址（ip和端口）
    :return:None
    """
    ip = input("请输入您发送主机的ip：(回车键结束)\n")
    port = int(input("请输入您发送主机的port：(回车键结束)\n"))
    content = input("请输入您发送信息内容：(回车键结束)\n")
    addr = (ip, port)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(content.encode(), addr)
    udp_socket.close()


def recev_message():
    """
    :param addr: 接收信息的主机地址
    :return:
    """
    addr = ("127.0.0.1", 8888)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(addr)
    data, ip_port= udp_socket.recvfrom(1024)
    print("您收到来自{}的消息：{}".format(ip_port, data.decode()))
    udp_socket.close()


if __name__ == '__main__':

    str = "\n\n--------------   菜单   --------------\n"
    str += "-------------1.发送信息---------------\n"
    str += "-------------2.退出程序---------------\n"

    # 子线程，单独接收信息
    t1 = threading.Thread(target=recev_message)
    # 设置子线程守护子线程
    t1.setDaemon(True)
    t1.start()

    while True:
        print(str)
        flag = int(input("请输入您要选择的功能:(如：1)\n"))

        if flag == 1:
            try:
                send_message()
                print("发送信息成功")
            except BaseException as e:
                print("发送信息失败：原因为", e)
        else:
            print("程序已退出...")
            break

