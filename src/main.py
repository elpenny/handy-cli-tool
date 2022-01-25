import typer
import command_groups.services as services

app = typer.Typer()
app.add_typer(services.app, name="services")

# Planned command groups:
# slew of commands related to running local env of services in docker
@app.callback()
def callback():
    """
    My handy cli app.
    It has few command groups.
    """

if __name__ == "__main__":
    app()
