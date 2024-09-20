import json
from models import task

def save(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)
        
def getAll(filename):
    tasks = []
    with open(filename, "r") as file:
        tasks = json.load(file)
    
    return tasks