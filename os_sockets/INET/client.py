import socket


def run_client_inet(message):
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    # BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    for x in range(100000):
        s.send(message)
        # data = s.recv(BUFFER_SIZE)
    s.close()

    # print("-----client: received data: {}".format(data))
