import pytest
from lib.todo import *

def test_check_todo_is_given():
    result = check_todo("#TODO: I need to do the hoovering")
    assert result == True
    
def test_check_todo_is_not_given():
    result = check_todo("Do the dishes")
    assert result == False
    
def test_check_todo_is_not_a_string():
    with pytest.raises(Exception) as e:
        check_todo(123456)
    error_message = str(e.value)
    assert error_message == "This is not a valid string"