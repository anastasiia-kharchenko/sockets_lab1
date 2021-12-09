import socket


def run_nonblocking_client(message):
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    # BUFFER_SIZE = 1024

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, TCP_PORT))
    for x in range(100000):
        sock.send(message)
