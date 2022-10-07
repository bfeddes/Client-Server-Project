import socket
import threading
PORT = 8080


def handle_client(sock, addr):
    try:
        print('<{}> thread to handle {}'.format(threading.current_thread().getName(), addr))

        chunks = []
        while True:
            data = sock.recv(4096)
            if not data:
                break
            chunks.append(data.decode('utf-8'))

        msg = ''.join(chunks)
        sock.sendall(msg.encode('utf-8'))
    except (ConnectionError, BrokenPipeError):
        print('Socket error')
    finally:
        print('<{}> - closed connection to {}'.format(threading.current_thread().getName(), addr))
        sock.shutdown(socket.SHUT_RDWR)
        sock.close


def listening():
    print('<{}> thread handling main loop'.format(threading.current_thread().getName()))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('0.0.0.0', PORT))
    s.listen(20)

    while True:
        client_sock, remote_addr = s.accept()
        print('<{}> - [+] connection from {}, spinning a new thread to handle it'.format(threading.current_thread()
                                                                                       .getName(), remote_addr))
        thread = threading.Thread(target=handle_client, args=[client_sock, remote_addr], daemon=True)
        thread.start()
