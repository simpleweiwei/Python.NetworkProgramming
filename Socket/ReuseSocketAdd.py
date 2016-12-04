import socket


# 重用套接字
def reuse_socket_add():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    old_reuse_state = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("Old: " + str(old_reuse_state))  # 为0，默认不可重用
    # 设置为可重用
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_reuse_state = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("New: " + str(new_reuse_state))  # 非o，可重用

    local_port = 8282
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('', local_port))
    srv.listen(1)
    print("listening: ", srv.getsockname())
    while True:
        try:
            connection, addr = srv.accept()
            print("Connected by", addr[0], addr[1])
        except KeyboardInterrupt:
            break
        except socket.error as err:
            print("err:" + err)


if __name__ == '__main__':
    reuse_socket_add()
