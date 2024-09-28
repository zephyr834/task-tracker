import click
from util.taskHelper import printTasks
from models.task import task
from services import taskService

_dbjson = "db/tasks.json"

@click.group()
@click.version_option(version='1.0.0')
def cli():
    "Task Tracker CLI"

@cli.command(name="add")
@click.argument("title")
@click.argument("description")
def add(title, description):
    "Add a new task"
    t = task(title, description)
    taskService.saveTask(_dbjson, t)
    click.echo("Succesfully added task")
    
@cli.command(name="update")
@click.argument("uid")
@click.argument("title")
@click.option(
    "-d",
    "--description",
    help="Updates the task description")
def update(uid, title, description):
    "Update the title or description of task"
    taskService.updateById(_dbjson, uid, title, description)
    
@cli.command(name="delete")
@click.argument("uid")
def delete(uid):
    "Delete a task"
    taskService.deleteById(_dbjson, uid)
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
    tasks = taskService.findAll(_dbjson, status)
    printTasks(tasks)
    
@cli.command(name="mark")
@click.argument("status")
@click.argument("uid")
def mark(status, uid):
    "Mark a task with an updated status"
    if isStatusValid(status):
        taskService.updateById(_dbjson, uid, status=status)
    else:
        print("Error: Status input is invalid.")
    
def isStatusValid(status):
    validStatus = { 
                    "todo", 
                    "in-progress", 
                    "done"
                    }
    return status in validStatus