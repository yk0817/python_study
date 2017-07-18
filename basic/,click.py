import click

@click.command()
def cmd():
    click.echo('hello,world!')

def main():
    cmd()


if __name__ == '__main__':
    main()
