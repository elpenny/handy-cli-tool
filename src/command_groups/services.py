from .text import help_text
import typer
from typing import List


app = typer.Typer()

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
    This command lets you tag current repository to trigger deployments.

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

@app.command()
def list():
    typer.echo("Listing deployable services and possible environment targets for this repository")

@app.command()
def verify():
    typer.echo("Checking which services source code was changed against main branch")

if __name__ == "__main__":
    app()
