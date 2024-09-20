import click
import task

@click.group()
@click.version_option(version='1.0.0')
def cli():
    "Task Tracker CLI"

@cli.command(name="add")
@click.argument("title")
def add(title):
    "Add a new task"
    
    click.echo(f"Succesfully added task: {title}")
    
@cli.command(name="update")
@click.argument("id")
@click.argument("title")
def update(id, title):
    "Update a task"
    click.echo(f"Succesfully updated task #{id}: {title}")
    
@cli.command(name="delete")
@click.argument("id")
def delete(id):
    "Delete a task"
    click.echo(f"Succesfully deleted task #{id}")
    
@cli.command(name="list")
@click.option(
    "--status",
    "-s",)
def list(status):
    "Lists all tasks by status"
    click.echo(f"Tasks with {status} status:")