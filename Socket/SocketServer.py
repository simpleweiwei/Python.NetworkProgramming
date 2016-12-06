import socket

host = 'localhost'
data_playload = 2048
backlog = 5


def socket_server(port):
    # AF_INET代表的是ipv4地址，SOCK_STREAM代表的是tcp
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print("bind address:", server_address)
    s.bind(server_address)
    s.listen(backlog)
    while True:
        client, address = s.accept() 
        # 接受连接并返回(client, address),其中client是新的套接字对象,用来接受同时也可以发送数据,address是连接客户端的地址,此时是阻塞状态
        # 注意进行数据交换的是新的套接字对象client,并不是刚开始创建的套接字对象
        data = client.recv(data_playload)
        if data:
            print("data:", data)  # data可以通过data.decode()进行解码
            client.send(data)  # 可以通过client.sendall(bytes('XXXXX',encoding='utf8')) 发送数据,注意python3中发送必须是bytes格式的
            print("sent {} bytes back to {}".format(data, address))
        client.close()


if __name__ == '__main__':
    socket_server(9900)
