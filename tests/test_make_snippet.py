from lib.make_snippet import *

def test_snipped_string():
    snipped_string = SnippedString()
    result = snipped_string.make_snippet("Hello my name is Sean what is your name?")
    assert result == "Hello my name is Sean ..."
    
def test_not_snipped_string():
    snipped_string = SnippedString()
    result = snipped_string.make_snippet("Hello")
    assert result == "Hello"