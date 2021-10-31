class TodoItem:
    def __init__(self, card):
        self.id = card["id"]
        self.status = card["status"]
        self.title = card["name"]
        self.last_edited = card["dateLastActivity"]
