from enum import Enum

class Status(Enum):
    TODO = "À faire"
    IN_PROGRESS = "En cours"
    DONE = "Fait"

class Priority(Enum):
    LOW = "Basse"
    MEDIUM = "Moyenne"
    HIGH = "Haute"

class TodoItem:
    def __init__(self):
        self.todo_items = []

    def create_todo_item(self, title, description, priority, due_date):
        todo_item = {
            "title": title,
            "description": description,
            "status": Status.TODO,
            "priority": priority,
            "due_date": due_date
        }
        self.todo_items.append(todo_item)

    def update_todo_item_status(self, todo_list_index, item_index, status):
        self.todo_items[todo_list_index][item_index]["status"] = status

    def update_todo_item_priority(self, todo_list_index, item_index, priority):
        self.todo_items[todo_list_index][item_index]["priority"] = priority

    def get_todo_items(self):
        return self.todo_items
