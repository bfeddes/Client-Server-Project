# Program 2
import click
import server
import client


@click.group()
def cli():
    pass


@cli.command()
@click.argument('n', default=50, type=int)
def load_test(n):
    client.load_testing(n)


@cli.command()
@click.argument('HOST', default='127.0.0.1')
@click.argument('PORT', default=8080, type=int)
@click.option('--i', is_flag=True, help='interactive mode')
def connect(host, port, i):
    '''connects to a TCP server on HOST PORT.'''
    click.echo('connecting to {} on port {}'.format(host, port))
    if i:
        click.echo("interactive mode")
        client.interactive_mode(host, port)
    else:
        client.single_line_mode(host, port)


@cli.command()
@click.argument('PORT', default=8080, type=int)
def listen(port):
    '''starts a TCP server'''
    click.echo('starting a TCP server on port {}'.format(port))
    s = server.listen_concurrent()
    server.handle_client(s)


if __name__ == '__main__':
    cli()
