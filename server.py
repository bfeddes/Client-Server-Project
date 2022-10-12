import socket
import threading


class ConnectionClosed(Exception):
    pass


def receive_line(conn):
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
    thread_count = 1
    while True:
        try:
            line = receive_line(conn)
            conn.sendall('Echo: {}'.format(line).encode('utf-8'))
        except ConnectionClosed:
            print('<Thread-{}> closed connection.'.format(thread_count))
            break


def listen():
    print('<{}> thread handling main loop'.format(threading.current_thread().getName()))
    thread_count = 1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('0.0.0.0', 8080))
    s.listen(20)
    while True:
        conn, remote_addr = s.accept()
        print('<Thread-{}> - [+] connection from {}, spinning a new thread to handle it.'.format
              (thread_count, remote_addr))
        thread = threading.Thread(target=handle_client, args=[conn], daemon=True)
        thread_count += 1
        thread.start()

