import typer
import services

app = typer.Typer()
app.add_typer(services.app, name="services")

# Planned commands:
# checkRequiredDeployments - runs only validation of changes in a branch against list of services
# slew of commands related to running local env of services in docker
@app.callback()
def callback():
    """
    My handy cli app.
    For now it has triggerbuild command 
    which tags git repo its ran in.
    """

if __name__ == "__main__":
    app()
