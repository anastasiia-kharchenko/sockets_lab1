import socket


def run_async_client(message):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(('127.0.0.1', 8080))
    for x in range(1):
        if message:
            server.send(message)
            response = server.recv(255)
            print(response)
    server.close()
