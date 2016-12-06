import socket

host = 'localhost'
port = 3434

# 注意客户端端口是系统分配的


def socket_client_udp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 第二个参数说明是采用UDP协议
    data = b"Hello udp message!"
    server_address = (host, port)
    s.sendto(data, server_address)
    print("sent ", data, "to ", server_address)
    s.close()


if __name__ == '__main__':
    socket_client_udp()
