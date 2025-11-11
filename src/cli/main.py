import typer

from src.models.category import Category
from src.models.task import Task
from src.models.tag import Tag

app = typer.Typer()


@app.command()
def hello(name, str):
    print(f"hi {name}")
