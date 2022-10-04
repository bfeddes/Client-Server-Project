def connect(host, port):
    click.echo('connecting to {} on port {}'.format(host, port))

    remote_server = ('127.0.0.1', 8080)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(remote_server)
    s.sendall('Kai'.encode('utf-8'))
    s.shutdown(socket.SHUT_WR)
    data = s.recv(2000)
    s.shutdown(socket.SHUT_RD)
    s.close()
    print('Got back: {}'.format(data.decode('utf')))