import typer
import sys
from .text import help_text
from typing import List
sys.path.append("..")
from subservices.configuration import loadConfig


app = typer.Typer()
@app.callback()
def main():
    """
    Manage microservices based in this repository
    """

# Planned features: 
# option to analyze repo and output warning if not all affected services are going to be tagged
# dry-run
# services and envs validation
# progress bars
# hints when input has errors

@app.command()
def tag(services: List[str] = typer.Argument(..., help=help_text["tag_services"]), 
        env: str = typer.Option(..., "--env", "-e", help=help_text["tag_env"]),
        noValidation: bool = typer.Option(False, "--no-validation", "-v", help=help_text["tag_validation"])):
    """
    tag services for deployments

    """
    if noValidation:
        typer.echo("Changed services validation is turned off.")
    typer.echo("Setting git tags to trigger deployment(s)")
    
    if 'all' in services:
        typer.echo(f"Deploying all services to {env} environment")
    else:
        typer.echo(f"Deploying to {env} environment.")
        typer.echo("Deploying following microservices:")
        for x in services:
            typer.echo(f"{x}")

    loadConfig()

@app.command()
def list():
    """
    list microservices based in this repository
    """
    typer.echo("Listing deployable services and possible environment targets for this repository")

@app.command()
def verify():
    """
    check which services must be deployed based on changes on active branch
    """
    typer.echo("Checking which services source code was changed against main branch")

if __name__ == "__main__":
    app()
