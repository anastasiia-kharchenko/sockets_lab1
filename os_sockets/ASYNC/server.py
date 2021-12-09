import asyncio
import socket


async def handle_client(client):
    loop = asyncio.get_event_loop()
    request = None
    for x in range(1):
        request = (await loop.sock_recv(client, 255))
        response = request
        await loop.sock_sendall(client, response)


async def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(8)
    server.setblocking(False)

    loop = asyncio.get_event_loop()
    print("server was started")
    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(handle_client(client))


def run_async():
    asyncio.run(run_server())
