import socket
import threading
PORT = 8080


class ConnectionClosed(Exception):
    pass


def receive_line(conn): # receive a single line that ends with a period
    chunks = []
    while True:
        data = conn.recv(2000)
        if not data:
            raise ConnectionClosed()

        chunks.append(data.decode('utf-8'))
        if ''.join(chunks).endswith('.'):
            break

    return ''.join(chunks)


def handle_client(conn):
    while True: #handle multiple lines until a disconnection
        try:
            line = receive_line(conn)
            conn.sendall('Echo: {}'.format(line).encode('utf-8'))
        except ConnectionClosed:
            break
        print('closed connection')


def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 8080))
    s.listen(20)
    while True:
        conn, remote_addr = s.accept()
        print('[+] connection from {}'.format(remote_addr))
        thread = threading.Thread(target=handle_client, args=[conn], daemon=True)
        thread.start()

