# File: lib/todo_items.py
class Todo():

    def __init__(self, task):
        self.task = task
        self.completed = False
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        self.completed = True
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass
    
    
