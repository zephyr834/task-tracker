import click
from util.taskHelper import printTasks
from models import task
from services import taskService

_filename = "db/tasks.json"

@click.group()
@click.version_option(version='1.0.0')
def cli():
    "Task Tracker CLI"

@cli.command(name="add")
@click.argument("title")
@click.argument("description")
def add(title, description):
    "Add a new task"
    t = task.task(title, description)
    taskService.saveTask(_filename, t)
    click.echo("Succesfully added task")
    
@cli.command(name="update")
@click.argument("uid")
@click.argument("title")
@click.argument("description")
def update(uid, title, description):
    "Update a task"
    taskService.updateById(_filename, uid, title, description)
    click.echo("Succesfully updated task")
    
@cli.command(name="delete")
@click.argument("uid")
def delete(uid):
    "Delete a task"
    taskService.deleteById(_filename, uid)
    click.echo("Deleted task")
    
@cli.command(name="list")
def list():
    "Lists all tasks by status"
    tasks = taskService.findAll(_filename)
    printTasks(tasks)
    
