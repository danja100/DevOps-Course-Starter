import os
from datetime import datetime
from dateutil.parser import parse


class TodoItem:
    def __init__(self, card):
        status = ""

<<<<<<< Updated upstream
        if card["idList"] == os.getenv("to_do_list"):
            status = "To Do"
        if card["idList"] == os.getenv("in_progress_list"):
=======
        if card["idList"] == os.getenv("LIST_ID_NOT_STARTED"):
            status = "Not Started"
        if card["idList"] == os.getenv("LIST_ID_IN_PROGRESS"):
>>>>>>> Stashed changes
            status = "In Progress"
        if card["idList"] == os.getenv("complete_list"):
            status = "Complete"

        self.id = card["idShort"]
        self.status = status
        self.title = card["name"]
        self.last_edited = parse(card["dateLastActivity"]).replace(tzinfo=None)
        self.due_date = (
            (parse(card["due"]).replace(tzinfo=None)).strftime("%d-%B-%Y")
            if type(card["due"]) == str
            else "No due date set"
        )
