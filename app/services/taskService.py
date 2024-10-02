from repositories import taskRepository
from datetime import datetime

def saveTask(filename, newTask):
    tasks = findAll(filename) 
    lastId = max(t['uid'] for t in tasks) if tasks else 0
    newTask['uid'] = lastId + 1
    tasks.append(newTask)
    taskRepository.saveJson(filename, tasks)

def findAll(filename, status=None):
    tasks = taskRepository.loadJson(filename)
    if status:
        tasks = [t for t in tasks if t['status'] == status]
    return tasks

def updateById(filename:str, uid:int, title=None, description=None, status=None):
    if title or description or status:
        tasks = findAll(filename)
        for t in tasks:
            if t['uid'] == uid:
                #print("Found uid")
                if title:
                    t['title'] = title
                if description:
                    t['description'] = description
                if status:
                    t['status'] = status
                t['updatedAt'] = datetime.now().isoformat()
                
                taskRepository.saveJson(filename, tasks)
                return
    
def deleteById(filename:str, uid:int):
    tasks = findAll(filename)
    tasks = [t for t in tasks if t['uid'] != uid]
    taskRepository.saveJson(filename, tasks)