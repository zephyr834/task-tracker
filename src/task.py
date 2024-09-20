from datetime import datetime

class Task:
    _id_counter = 1
    
    def __init__(self, title, description):
        self.id = Task._id_counter
        self.title = title
        self.description = description
        self.status = "todo"
        self.createdAt = datetime.now()
        self.updatedAt = datetime.now()
        
        Task._id_counter += 1