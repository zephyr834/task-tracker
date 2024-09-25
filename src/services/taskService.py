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

def updateById(filename, uid, title=None, description=None, status=None):
    if title or description or status:
        tasks = findAll(filename)
        for t in tasks:
            if t['uid'] == int(uid):
                #print("Found uid")
                if title:
                    t['title'] = title
                if description:
                    t['description'] = description
                if status:
                    t['status'] = status
                t['updatedAt'] = datetime.now().isoformat()
                
                taskRepository.save(filename, tasks)
                return
    
def deleteById(filename, uid):
    tasks = findAll(filename)
    tasks = [t for t in tasks if t['uid'] != uid]
    taskRepository.save(filename, tasks)