from model.todo_list import TodoList
from view.todo_view import TodoView

class TodoListController:
    def __init__(self):
        self.todo_list = TodoList()
        self.view = TodoView()

    def add_todo_list(self, todo_list_name):
        self.todo_list.create_todo_list(todo_list_name)
        self.view.update_todo_lists(self.todo_list.get_todo_lists())

    def get_todo_lists(self):
        return self.todo_list.get_todo_lists()
