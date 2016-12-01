import socket


# 通过socket创建一个套接字实例并设置套接字超时时间
def set_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Default socket timeout： {}".format(s.gettimeout()))
    s.settimeout(120)
    print("Current socket timeout： {}".format(s.gettimeout()))


if __name__ == '__main__':
    set_socket_timeout()
