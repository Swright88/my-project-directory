from lib.string_builder import *

def test_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""
    
def test_string_builder():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.output() == "hello"
    assert string_builder.size() == 5
