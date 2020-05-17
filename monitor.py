#! /usr/bin/python3
import psutil
import datetime


def info():
    cpu_per = psutil.cpu_percent(interval=0.5)

    memory_info = psutil.virtual_memory()

    disk_info = psutil.disk_usage("/")
    net_info = psutil.net_io_counters()

    current_time = datetime.datetime.now().strftime("%F %T")

    log_str = "-----------------------------------------------------------\n"
    log_str += "| 监控时间:{}                             | \n".format(current_time)
    log_str += "| CPU使用率:{}%                                         | \n".format(cpu_per)
    log_str += "| CPU核心数目:{}核                                            | \n".format(psutil.cpu_count(logical=False))
    log_str += "| 內存容量:{:.2f}G                                           | \n".format(memory_info.total/(1024)**3)
    log_str += "| 內存使用率: {}%                                      | \n".format(memory_info.percent)
    log_str += "| 硬盘容量:{:.2f}G                                         | \n".format(disk_info.total/(1024)**3)
    log_str += "| 硬盘使用率: {}%                                          | \n".format(disk_info.percent)
    log_str += "| 网络收发量:收{:.4f} KB｜ 发{:.4f} KB                     | \n".format(net_info.bytes_recv/(1024)**2*8, net_info.bytes_sent/(1024)**2*8)
    log_str += "----------------------------------------------------------\n"

    return log_str


if __name__ == '__main__':
    log_str = info()
    print(log_str)
    f = open("log.txt", "a")
    f.write(log_str)
    f.write("\n\n")
    f.close()
