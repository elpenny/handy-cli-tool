import typer
from typing import List

app = typer.Typer()

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

@app.command()
def list():
    typer.echo("Listing services in this repository")

@app.command()
def verify():
    typer.echo("Checking which services source code was changed against main branch")

if __name__ == "__main__":
    app()
