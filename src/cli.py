import click
from models.task import task
from services import taskService
import random

filename = "db/tasks.json"

@click.group()
@click.version_option(version='1.0.0')
def cli():
    "Task Tracker CLI"

@cli.command(name="add")
@click.argument("title")
@click.argument("description")
def add(title, description):
    "Add a new task"
    uId = random.randint(1, 100)
    t = task(uId, title, description)
    taskService.saveTask(filename, t)
    click.echo(f"Succesfully added task!")
    
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
def list(status):
    "Lists all tasks by status"
    tasks = taskService.findAll(filename)
    print(tasks)