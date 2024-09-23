from repositories import taskRepository
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
            break
    taskRepository.save(filename, tasks)