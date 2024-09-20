from repositories import taskRepository
#from models import task

def saveTask(filename, newTask):
    tasks = []
    tasks.extend( taskRepository.getAll(filename) )
    tasks.append(newTask)
    taskRepository.save(filename, tasks)

def findAll(filename):
    return taskRepository.getAll(filename)
