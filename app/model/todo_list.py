from datetime import datetime

class TodoList:
    def __init__(self):
        self.todo_lists = []

    def create_todo_list(self, name):
        todo_list = {
            "name": name,
            "creation_date": datetime.now(),
            "archive_date": None
        }
        self.todo_lists.append(todo_list)

    def get_todo_lists(self):
        return self.todo_lists
