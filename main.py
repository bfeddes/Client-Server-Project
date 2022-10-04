# Brian Feddes
# Client-Server Computing
# Professor Safwan Omari
# Echo client-server
import click
import server
import client

# ***NEED TO WORK ON INTERACTIVE MODE.***


@click.group()
def cli():
    pass


@cli.command()
@click.argument('HOST', default='127.0.0.1')
@click.argument('PORT', default=8080, type=int)
@click.option('--i', is_flag=True, help='interactive mode')
def connect(host, port, i):
    '''connects to a TCP server on HOST PORT. defaults to localhost 8080'''
    click.echo('connecting to {} on port {}'.format(host, port))
    if i:
        click.echo("interactive mode")
        client.interactive_mode(host, port)
    else:
        client.single_line_mode(host, port)


@cli.command()
@click.argument('PORT', default=8080, type=int)
@click.option('--port', type=int, help='specify port-number')
def listen(port, host):
    '''run in server mode and listens on port --port. defaults to port 8080'''
    click.echo('starting a TCP server on port {}'.format(port))
    server.handle_client(host, port)


if __name__ == '__main__':
    cli()
