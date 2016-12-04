import socket


# 设置socket为阻塞模式或非阻塞模式
# 类似一个简单的服务器
def set_socket_blocking():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)  # 设置为阻塞模式，如果为0则是非阻塞模式
    s.settimeout(0.5)
    s.bind(("127.0.0.1", 0))

    sock_add = s.getsockname()
    print("socket监听的地址", sock_add)
    while 1:
        s.listen(1)


if __name__ == '__main__':
    set_socket_blocking()
