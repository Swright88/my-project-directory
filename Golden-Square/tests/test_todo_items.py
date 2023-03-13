from lib.todo_items import *

""" Given a task
we should add the task to the list of todos """

def test_complete_false():
    Task_1 = Todo("shopping")
    assert Task_1.completed == False
    
def test_mark_completed():
    Task_1 = Todo("shopping")
    Task_1.mark_complete()
    assert Task_1.completed == True