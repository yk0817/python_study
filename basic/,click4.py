import click
# サブコマンドで色々な操作をサポートする。

@click.group()
def cmd():
    pass

@cmd.command()
def english():
    click.echo('hello,world')

@cmd.command()
def japanese():
    click.echo('konnichwa,sekai')

def main():
    cmd()

if __name__ == '__main__':
    main()
