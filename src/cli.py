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
@click.option(
    "-d",
    "--description",
    help="Updates the task description")
def update(uid, title, description):
    "Update a task"
    taskService.updateById(_filename, uid, title, description)
    
@cli.command(name="delete")
@click.argument("uid")
def delete(uid):
    "Delete a task"
    taskService.deleteById(_filename, uid)
    click.echo("Deleted task")
    
@cli.command(name="list")
@click.option(
    "-s",
    "--status",
    help="Filter tasks by status: todo, in-progress, done",
)
def list(status):
    "Lists all tasks"
    tasks = []
    if status:
        tasks = taskService.findAllByStatus(_filename, status) 
    else:
        tasks = taskService.findAll(_filename) 
    printTasks(tasks)
    
