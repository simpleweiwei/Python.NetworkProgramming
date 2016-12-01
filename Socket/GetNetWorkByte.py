import socket

# 通过socket进行网络字节数据和主机字节数据转换


def get_net_byte_info():
    data = 2016
    print("原始数据：{} LONG > host bytes: {} LONG > network bytes:{}".format(data, socket.ntohl(data), socket.htonl(data)))
    print("原始数据：{} SHORT > host bytes: {} SHORT > network bytes:{}".format(data, socket.ntohs(data), socket.htons(data)))


if __name__ == '__main__':
    get_net_byte_info()

"""
output:

原始数据：2016 LONG > host bytes: 3758555136 LONG > network bytes:3758555136
原始数据：2016 SHORT > host bytes: 57351 SHORT > network bytes:57351

"""
