import pytest
from lib.present import *

def test_if_wrapped():
    present = Present()
    present.wrap(55)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."


def test_if_unwrapped():
    present = Present()
    with pytest.raises(Exception) as e: # <-- New code
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
    
