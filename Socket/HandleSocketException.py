import socket
import sys


# 虽然访问的资源不存在，但是依然可以连接成功，注意socket异常的处理
def main():
    # 创建socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err_msg:
        print(err_msg)
        sys.exit(1)

    # 连接某个主机
    try:
        s.connect(("www.python.org", 80))
    except socket.gaierror as err_gai:  # 提供的地址不存在
        print(err_gai)
        sys.exit(1)
    except socket.error as err:
        print(err)
        sys.exit(1)

    # 发送数据
    try:
        s.sendall(b"GET xx.py HTTP/1.0\r\n\r\n")
    except socket.error as err:
        print(err)
        sys.exit(1)

    # 接收数据
    while 1:
        try:
            buf = s.recv(2048)
        except socket.error as err:
            print(err)
            sys.exit(1)
        if not len(buf):
            break
        sys.stdout.write(buf.decode('utf-8'))


if __name__ == '__main__':
    main()
