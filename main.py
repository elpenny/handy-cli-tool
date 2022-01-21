import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def triggerbuild(tag: str):
    typer.echo(f"Entered desired tag {tag}")


if __name__ == "__main__":
    app()