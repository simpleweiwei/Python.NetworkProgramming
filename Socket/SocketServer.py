import socket

host = 'localhost'
data_playload = 2048
backlog = 5


def socket_server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print("bind address:", server_address)
    s.bind(server_address)
    s.listen(backlog)
    while True:
        client, address = s.accept()
        data = client.recv(data_playload)
        if data:
            print("data:", data)
            client.send(data)
            print("sent {} bytes back to {}".format(data, address))
        client.close()


if __name__ == '__main__':
    socket_server(9900)
