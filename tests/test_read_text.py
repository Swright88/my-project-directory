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





# """Given a number of words
# It returns the amount of minutes it will take to read. """
# minutes_to_read_text(1000) == "It will take 5 minutes to read 1000 words."

# """Given a negative number
# It returns an Exception error"""
# minutes_to_read_text_negative(-200) == Exception "You can not have a negative number of words!"

# """Given any type other than int
# It returns an Exception error """
# minutes_to_read_text_type(string) == Exception "You have not entered a number in the correct format"
