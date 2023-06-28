from model.todo_item import TodoItem
from view.todo_view import TodoView

class TodoItemController:
    def __init__(self):
        self.todo_item = TodoItem()
        self.view = TodoView()

    def add_todo_item(self, todo_list_index, item_title, item_description, item_priority, item_due_date):
        self.todo_item.create_todo_item(item_title, item_description, item_priority, item_due_date)
        self.view.update_todo_items(todo_list_index, self.todo_item.get_todo_items())

    def update_todo_item_status(self, todo_list_index, item_index, status):
        self.todo_item.update_todo_item_status(todo_list_index, item_index, status)
        self.view.update_todo_items(todo_list_index, self.todo_item.get_todo_items())

    def update_todo_item_priority(self, todo_list_index, item_index, priority):
        self.todo_item.update_todo_item_priority(todo_list_index, item_index, priority)
        self.view.update_todo_items(todo_list_index, self.todo_item.get_todo_items())
