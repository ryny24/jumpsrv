import socket

#print(is_port_in_use(10901))
# 10900
# 10901

import socket
from contextlib import closing
def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(1)
        if sock.connect_ex((host, port)) == 0:
            print("Port is open")
        else:
            print("Port is not open")


print(check_socket('localhost',10900))
print(check_socket('localhost',10901))
