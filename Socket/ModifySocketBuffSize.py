import socket

# 修改套接字发送和接收缓冲区大小

SEND_SIZE = 4096
REV_SIZE = 4096


def modify_socket_buff_size():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 打印默认缓冲区大小
    send_buff_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Default send buff size： {}".format(send_buff_size))
    rev_buff_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Default rev buff size： {}".format(rev_buff_size))
    # 修改缓冲区大小
    s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)  # 非必需
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_SIZE)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, REV_SIZE)
    # 打印现在（修改后）缓冲区大小
    now_send_buff_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Now send buff size： {}".format(now_send_buff_size))
    now_rev_buff_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print("Now rev buff size： {}".format(now_rev_buff_size))


if __name__ == '__main__':
    modify_socket_buff_size()
