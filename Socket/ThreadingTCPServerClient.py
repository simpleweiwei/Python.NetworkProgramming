import socket

ip_port = ('localhost', 2016)
s = socket.socket()
s.connect(ip_port)
welcome_msg = s.recv(1024)
print('from server:', welcome_msg.decode())

while True:
    send_data = input('>>:').strip()
    print("type:", type(send_data))
    s.send(bytes(send_data, encoding='utf8'))
    if send_data == 'exit':
        break
    if len(send_data) == 0:
        continue
    recv_data = s.recv(1024)
    print(str(recv_data, encoding='utf8'))
s.close()
