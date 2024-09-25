from datetime import datetime

def getReadableDateTime(isoDateTime):
    # Convert the ISO string to a datetime object
    dt_object = datetime.fromisoformat(isoDateTime)

    readable_format = dt_object.strftime("%B %d, %Y %I:%M %p")
    return readable_format

def printTasks(tasks):
    print(f"{'UID':^15} | {'Title':^15}| {'Description':^15}| {'Status':^15}| {'Created At':^30}| {'Updated At':^30}|")
    for t in tasks:
        createdAt = getReadableDateTime(t['createdAt'])
        updatedAt = getReadableDateTime(t['updatedAt'])
        print(f"{t['uid']:^15} | {t['title']:^15}| {t['description']:^15}| {t['status']:^15}| {createdAt:^30}| {updatedAt:^30}|")