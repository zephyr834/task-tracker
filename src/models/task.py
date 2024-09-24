from datetime import datetime
import time
import random

def task(title, description):
    uid = str(int(time.time())) + str(random.randint(1000, 9999))
    defaultStatus = "todo"
    return {
        "uid": uid,
        "title": title,
        "description": description,
        "status": defaultStatus,
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
