import pytest
from lib.grammar_check import *

def test_grammar_check_true():
    result = grammar_check("Hello how are you today?")
    assert result == True
    
def test_grammar_check_false():
    result2 = grammar_check("hi nice to meet you") 
    assert result2 == False