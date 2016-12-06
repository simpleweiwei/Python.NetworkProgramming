import socketserver

# ThreadingTCPServer实现的Soket服务器内部会为每个client创建一个 “线程”，该线程用来和客户端进行交互


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        # print self.request,self.client_address,self.server
        conn = self.request
        conn.sendall(bytes('欢迎致电 10086，请输入1xxx,0转人工服务.', 'utf8'))
        flag = True
        while flag:
            data = conn.recv(1024)
            print(data.decode())
            print("type:", type(data))
            result = data.decode()
            if result == 'exit':
                flag = False
            elif result == 'a':
                conn.sendall(bytes('通过可能会被录音.balabala一大推', 'utf8'))
            else:
                conn.sendall(bytes('请重新输入.', 'utf8'))


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('localhost', 2016), MyServer)
    server.serve_forever()
