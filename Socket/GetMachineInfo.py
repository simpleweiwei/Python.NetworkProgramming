import socket


# 通过socket的类方法获取主机名和IP
def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("主机名： {}".format(host_name))
    print("IPV4地址： {}".format(ip_address))


if __name__ == '__main__':
    print_machine_info()
