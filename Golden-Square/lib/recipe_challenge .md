# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.



## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._
def check_for_todo(string):
    return True or False

    Parameters: Text which should contain #TODO

    Return Value: Boolean value of either True or False

    Side Effects: If the text is not passed as a string we will expect an Exception error to be raised


```python


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""Given a passage of text as a string
It returns True if it contains #TODO """
check_todo_is_given("#TODO: I need to do the hoovering") == True

"""Given a passage of text as a string
It returns False as it does not contain #TODO"""
check_todo_not_given("Do the dishes") == False

"""Given a value that is not a string
It raises an Exception error due to invalid type"""
check_todo_not_a_string(123456) == Exception "This is not a valid string"


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

mport pytest
from lib.read_text import *

def test_minutes_to_read():
    assert minutes_to_read_text(1000) == "It will take 5 minutes to read 1000 words!"
    
def test_minutes_to_read_text_negative():
    with pytest.raises(Exception) as e:
        minutes_to_read_text(-1000)
    error_message = str(e.value)
    assert error_message == "You can not have a negative number of words!"
    
def test_minutes_to_read_text_type():
    with pytest.raises(Exception) as e:
        minutes_to_read_text("hello")
    error_message = str(e.value)
    assert error_message == "You have not entered a number in the correct format"
```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

<!-- END GENERATED SECTION DO NOT EDIT -->