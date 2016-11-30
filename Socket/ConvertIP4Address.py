import socket
from binascii import hexlify


# 通过socket将ipv4转换为其他格式
# 调用hexlify（）是为了将二进制数据转换为十六进制
def convert_ip4_address():
    ip_list = ["127.0.0.1", "192.168.0.1"]
    for ip in ip_list:
        packed_ip = socket.inet_aton(ip)
        unpacked_ip = socket.inet_ntoa(packed_ip)
        print(type(packed_ip))
        print("IP：{} Packed: {} Unpacked: {}".format(ip, hexlify(packed_ip), unpacked_ip))


if __name__ == '__main__':
    convert_ip4_address()

"""
output:

<class 'bytes'>
IP：127.0.0.1 Packed: b'7f000001' Unpacked: 127.0.0.1
<class 'bytes'>
IP：192.168.0.1 Packed: b'c0a80001' Unpacked: 192.168.0.1

"""