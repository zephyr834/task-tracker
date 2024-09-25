from repositories import taskRepository
from datetime import datetime

def saveTask(filename, newTask):
    tasks = findAll(filename) 
    lastId = max(t['uid'] for t in tasks) if tasks else 0
    newTask['uid'] = lastId + 1
    tasks.append(newTask)
    taskRepository.save(filename, tasks)

def findAll(filename):
    return taskRepository.getAll(filename)

def findAllByStatus(filename, status):
    tasks = findAll(filename)
    tasks = [t for t in tasks if t['status'] == status]
    return tasks

def updateById(filename, uid, title, description):
    tasks = findAll(filename)
    for t in tasks:
        if t['uid'] == uid:
            t['title'] = title
            t['description'] = description
            t['updatedAt'] = datetime.now().isoformat()
            break
    taskRepository.save(filename, tasks)
    
def deleteById(filename, uid):
    tasks = findAll(filename)
    tasks = [t for t in tasks if t['uid'] != uid]
    taskRepository.save(filename, tasks)