import click
import requests
sdfsdf

@click.group()
def cli():
    pass
@cli.command(help = 'Checks if passed url is up and working')
#@click.option('--url', default="http://satvikkishore.com", help=|'Checks if passed url is up and working')
@click.argument('url')
def url(url):
    try:
        r = requests.head(url)
    except requests.exceptions.ConnectionError:
        click.echo(f"Not reachable lol")
        return
    except requests.exceptions.MissingSchema:
        click.echo(f"You probably meant http://{url}. Don't be lazy")
        return
    if r.status_code in {200,301}:
        click.echo("Is up")
        pass
    
    else:
        click.echo(f"status code was {r.status_code}")
        pass

@cli.command(help='checks if passed concept/object is physically above you')
@click.argument('concept')
def concept(concept):
    if concept == "@@@@":
        click.echo("Nor argument passed")
    elif concept in ["sky","space","planes","aircraft","clouds","ozone layer","stratosphere"]:
        click.echo("Yes!")
        pass
    else:
        click.echo("Probably not. If you think it is, take it up with the developer")
        pass
    
if __name__ == "__main__":
    cli()
