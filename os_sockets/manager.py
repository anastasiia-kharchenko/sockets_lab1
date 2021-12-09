import threading
import time

from ASYNC.client import run_async_client
from ASYNC.server import run_async
from INET.client import run_client_inet
from INET.server import run_server_inet
from NONBlock.client import run_nonblocking_client
from NONBlock.server import run_nonblocking_server

message = b'Hello, World Hello, World Hello, World'


def run_inet_socket():
    th1 = threading.Thread(target=run_server_inet)
    th2 = threading.Thread(target=run_client_inet, args=(message,))

    th1.start()
    th2.start()

    th1.join()
    th2.join()


def run_nonblocking_socket():
    th1 = threading.Thread(target=run_nonblocking_server)
    th2 = threading.Thread(target=run_nonblocking_client, args=(message,))
    th3 = threading.Thread(target=run_nonblocking_client, args=(message,))
    th4 = threading.Thread(target=run_nonblocking_client, args=(message,))

    th1.start()
    th2.start()
    # th3.start()
    # th4.start()

    th1.join()
    th2.join()
    # th3.join()
    # th4.join()


def run_async_socket():
    # th1 = threading.Thread(target=run_async)
    th2 = threading.Thread(target=run_async_client, args=(message,))
    th3 = threading.Thread(target=run_async_client, args=(message,))

    # th1.start()
    th2.start()
    th3.start()

    # th1.join()
    th2.join()
    th3.join()


start_time = time.time()
run_inet_socket()
print("INET(blocking)", time.time() - start_time, "seconds")

start_time = time.time()
run_nonblocking_socket()
print("INET(non-bLocking)", time.time() - start_time, "seconds")

# start_time = time.time()
# run_async_socket()
# print(time.time() - start_time, "seconds")
