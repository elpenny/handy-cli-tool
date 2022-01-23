from multiprocessing.dummy import Array
import typer
from typing import List

app = typer.Typer()

@app.callback()
def callback():
    """
    My handy cli app.
    For now it has triggerbuild command 
    which tags git repo its ran in.
    """

@app.command()
def tag(services: List[str], env: str = typer.Option(...)):
    typer.echo("Setting git tags to trigger deployment(s)")
    typer.echo(f"Deploying to {env} environment.")
    typer.echo("Deploying following microservices:")
    for x in services:
        typer.echo(f"{x}")


if __name__ == "__main__":
    app()