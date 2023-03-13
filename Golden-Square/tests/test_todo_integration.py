from lib.todo_list import *

""" Given the call to return the list of Todo's 
still to be completed (incomplete):
We get back an empty list if no items have been added """

def test_incomplete_list_empty():
    todo_list = TodoList()
    assert todo_list.incomplete() == []
    
""" Given the call to return the list of Todo's 
that have been completed (complete):
We get back an empty list if no items have been added """

def test_complete_list_empty():
    todo_list = TodoList()
    assert todo_list.complete() == []
    
    

def test_add_function():
    task1 = Todo("Task_1")
    todo_list = TodoList()
    todo_list.add(task1)
    assert todo_list.list_of_todo == [task1]


def test_give_up():
    task1 = Todo("Task_1")
    todo_list = TodoList()
    todo_list.add(task1)
    task2 = Todo("Task_2")
    todo_list.add(task2)
    todo_list.give_up()
    assert todo_list.complete() == [task1, task2]
    
def test_completed():
    task1 = Todo("Task_1")
    todo_list = TodoList()
    todo_list.add(task1)
    task2 = Todo("Task_2")
    todo_list.add(task2)
    task1.mark_complete()
    assert todo_list.complete() == [task1]
    
def test_incompleted():
    task1 = Todo("Task_1")
    todo_list = TodoList()
    todo_list.add(task1)
    task2 = Todo("Task_2")
    todo_list.add(task2)
    assert todo_list.incomplete() == [task1, task2]
    