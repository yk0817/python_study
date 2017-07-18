import click

@click.command()
@click.argument('name')

def cmd(name):
    msg = 'hello,{name}!'.format(name=name)
    click.echo(msg)

def main():
    cmd()

if __name__ == '__main__':
    main()
