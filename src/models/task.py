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

def getReadableDateTime(isoDateTime):
    # Convert the ISO string to a datetime object
    dt_object = datetime.fromisoformat(isoDateTime)

    readable_format = dt_object.strftime("%B %d, %Y %I:%M %p")
    return readable_format

def printTasks(tasks):
    print(f"{'UID':^15} | {'Title':^15}| {'Description':^15}| {'Status':^15}| {'Created At':^30}| {'Updated At':^30}|")
    for t in tasks:
        createdAt = getReadableDateTime(t['createdAt'])
        updatedAt = getReadableDateTime(t['createdAt'])
        print(f"{t['uid']:^15} | {t['title']:^15}| {t['description']:^15}| {t['status']:^15}| {createdAt:^30}| {updatedAt:^30}|")