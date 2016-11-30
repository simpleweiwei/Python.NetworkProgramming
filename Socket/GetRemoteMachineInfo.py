import socket

# 通过socket的类方法获取远程主机的IP
# 此方法很多时候不一定能够得到ip


def print_remote_machine_info():
    remote_host = "http://fund.eastmoney.com"
    try:
        print("远程主机的IPV4地址： {}".format(socket.gethostbyname(remote_host)))
    except socket.error as err:
        print(err)


if __name__ == '__main__':
    print_remote_machine_info()
