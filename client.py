import socket
import time


def single_line_mode(host, port):
    '''Allows for singular call and response from echo server'''

    remote_server = (host, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(remote_server)
    user_text = input('Send to echo server:')
    s.sendall('{}.'.format(user_text).encode('utf-8'))
    data = s.recv(2000)
    s.shutdown(socket.SHUT_WR)
    s.shutdown(socket.SHUT_RD)
    s.close()
    print('Got back: {}'.format(data.decode('utf')))


def interactive_mode(host, port):
    remote_server = (host, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(remote_server)
    user_text = ""

    while user_text != "quit.":
        user_text = input("Enter your message for the client to send to the server: ")
        user_text = '{}.'.format(user_text)
        s.sendall(user_text.encode('utf-8'))
        data = s.recv(2000)
        print('got back {}'.format(data.decode("utf")))


def load_testing(n):
    for i in range(n):
        start = time.time()
        remote_server = ('127.0.0.1', 8080)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(remote_server)
        user_text = "load testing"
        s.sendall('{}.'.format(user_text).encode('utf-8'))
        data = s.recv(2000)
        s.shutdown(socket.SHUT_WR)
        s.shutdown(socket.SHUT_RD)
        s.close()
        print('Got back: {}'.format(data.decode('utf')))
        rounded_num = round((time.time() - start) * 1000, 2)
        print("CON-{}: duration {}ms".format(i+1, rounded_num))
