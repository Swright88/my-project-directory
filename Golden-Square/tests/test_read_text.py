import pytest
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





