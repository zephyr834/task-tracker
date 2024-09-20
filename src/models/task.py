from datetime import datetime

def task(id, title, description):
    return {
        "id": id,
        "title": title,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }