import socket

host = 'localhost'
port = 3434


def socket_server_udp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 第二个参数说明是采用UDP协议
    server_address = (host, port)
    print("bind address:", server_address)
    s.bind(server_address)  # 绑定即可
    while True:
        data, address = s.recvfrom(1024)
        print("Received: {} from {}".format(data, str(address)))
    s.close()


if __name__ == '__main__':
    socket_server_udp()
