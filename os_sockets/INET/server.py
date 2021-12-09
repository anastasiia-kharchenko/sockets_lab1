import socket


def run_server_inet():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.setblocking(1)
    s.listen(1)

    conn, addr = s.accept()
    # print("-----server: Connection address: {}".format(addr))
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        # print("-----server: received data: {}".format(data))
        # conn.send(data)  # echo
    conn.close()
