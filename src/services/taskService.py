from repositories import taskRepository
#from models import task

def saveTask(filename, newTask):
    taskRepository.save(filename, newTask)

def findAll(filename):
    return taskRepository.getAll()