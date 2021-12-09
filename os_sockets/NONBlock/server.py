import socket
import select


def run_nonblocking_server():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(0)
    sock.bind((TCP_IP, TCP_PORT))
    sock.listen(5)
    # print("Server was started...")

    inputs = [sock]
    while inputs:
        # Wait for at least one of the sockets to be ready for processing
        # start select Monitor
        readable, writable, exceptional = select.select(inputs, [], inputs)
        # Handle inputs
        # Loop to determine if there is a client connection in, When a client connection comes in select Will trigger
        for s in readable:
            # Determine if the current trigger is a sock object?, When the triggered object is a sock-side object,Explain that a new client is connected in
            if s is sock:
                # A "readable" socket is ready to accept a connection
                conn, addr = s.accept()
                # Add client objects to the list of listeners, When the client sends a message select Will trigger
                inputs.append(conn)
            else:
                # Old users send messages, Processing acceptance
                # Because the server receives the client connection request when the client connection comes in, the client is added to the listening list.(input_list), Client sending message will trigger
                data = s.recv(BUFFER_SIZE)
                if data:
                    continue
                else:
                    inputs.remove(s)
                    s.close()
        if len(inputs) == 1:
            break
    sock.close()
