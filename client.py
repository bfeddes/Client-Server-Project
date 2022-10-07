import socket


def single_line_mode(host, port):

    remote_server = (host, port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(remote_server)
    message = input("Enter your message for the client to send to the server: ")

    s.sendall(message.encode('utf-8'))
    s.shutdown(socket.SHUT_WR)
    data = s.recv(2000)
    s.shutdown(socket.SHUT_RD)
    s.close()
    print('Got back: {}'.format(data.decode('utf')))


def interactive_mode(host, port):
    remote_server = (host, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(remote_server)
    message = ""

    while message != "quit.":
        message = input("Enter your message for the client to send to the server: ")
        message = "{}.".format(message)
        s.sendall(message.encode('utf-8'))
        data = s.recv(2000)
        print('Got back {}'.format(data.decode('utf')))

    s.shutdown(socket.SHUT_WR)
    s.shutdown(socket.SHUT_RD)
    s.close()
