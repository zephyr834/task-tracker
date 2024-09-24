from repositories import taskRepository
from datetime import datetime
#from models import task

def saveTask(filename, newTask):
    tasks = taskRepository.getAll(filename) 
    tasks.append(newTask)
    taskRepository.save(filename, tasks)

def findAll(filename):
    return taskRepository.getAll(filename)

def updateById(filename, uid, title, description):
    tasks = taskRepository.getAll(filename)
    for t in tasks:
        if t['uid'] == uid:
            t['title'] = title
            t['description'] = description
            t['updatedAt'] = datetime.now().isoformat()
            break
    taskRepository.save(filename, tasks)
    
def deleteById(filename, uid):
    tasks = taskRepository.getAll(filename)
    tasks = [t for t in tasks if t['uid'] != uid]
    taskRepository.save(filename, tasks)