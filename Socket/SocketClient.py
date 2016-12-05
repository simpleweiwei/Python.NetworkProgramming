import socket
import sys
import argparse

host = 'localhost'


def socket_client(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print("connecting address:", server_address)
    s.connect(server_address)
    try:
        message = b"python 2016"
        s.sendall(message)
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = s.recv(16)
            amount_received += len(data)
            print("received:", data)
    except socket.error as err:
        print(err)
    except Exception as e:
        print(e)
    finally:
        s.close()


if __name__ == '__main__':
    socket_client(9900)
