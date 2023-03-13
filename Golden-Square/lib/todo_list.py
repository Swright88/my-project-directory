from lib.todo_items import *
# File: lib/todo_list.py
class TodoList():
    def __init__(self):
        self.list_of_todo = []
        self.complete_list = []
        self.incomplete_list = []
        pass

    def add(self, todo):
        self.list_of_todo.append(todo)
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass

    def incomplete(self):
        for entry in self.list_of_todo:
            if entry.completed == False:
                self.incomplete_list.append(entry)
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return self.incomplete_list
        pass

    def complete(self):
        for entry in self.list_of_todo:
            if entry.completed == True:
                self.complete_list.append(entry)
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return self.complete_list
        pass

    def give_up(self):
        for entry in self.list_of_todo:
            entry.mark_complete()  
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass