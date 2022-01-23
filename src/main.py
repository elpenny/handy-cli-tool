from multiprocessing.dummy import Array
import typer
from typing import List

app = typer.Typer()

# Planned commands:
# checkRequiredDeployments - runs only validation of changes in a branch against list of services
# slew of commands related to running local env of services
@app.callback()
def callback():
    """
    My handy cli app.
    For now it has triggerbuild command 
    which tags git repo its ran in.
    """

# This should be subcommand to command "services"
# Planned features: 
# option to analyze repo and output warning if not all affected services are going to be tagged
# dry-run
# services and envs validation
# progress bars
# hints when input has errors
@app.command()
def tag(services: List[str], env: str = typer.Option(...)):
    typer.echo("Setting git tags to trigger deployment(s)")
    if 'all' in services:
        typer.echo(f"Deploying all services to {env} environment")
    else:
        typer.echo(f"Deploying to {env} environment.")
        typer.echo("Deploying following microservices:")
        for x in services:
            typer.echo(f"{x}")

# This is also part os "services" command
@app.command()
def list():
    typer.echo("Listing services in this repository")

if __name__ == "__main__":
    app()
