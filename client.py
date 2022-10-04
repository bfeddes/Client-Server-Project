import socket


def single_line_mode(host, port):

    remote_server = (host, port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(remote_server)
    user_text = input("Enter your message for the client to send to the server: ")

    s.sendall(user_text.encode('utf-8'))
    s.shutdown(socket.SHUT_WR)
    data = s.recv(2000)
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

    s.shutdown(socket.SHUT_WR)
    s.shutdown(socket.SHUT_RD)
    s.close()