import socket

# 模拟web服务器


def handle_request(client):
    # 接收请求
    buf = client.recv(1024)
    print(buf)
    # 返回信息
    client.send(bytes('<h1>This is a socket web server!</h1>', 'utf8'))


def main():
    # 创建sock对象
    sock = socket.socket()
    # 监听80端口
    sock.bind(('localhost', 8000))
    # 最大连接数
    sock.listen(5)
    print('welcome nginx')
    # 循环
    while True:
        # 等待用户的连接,默认accept阻塞当有请求的时候往下执行
        connection, address = sock.accept()
        # 把连接交给handle_request函数
        handle_request(connection)
        # 关闭连接
        connection.close()


if __name__ == '__main__':
    main()
