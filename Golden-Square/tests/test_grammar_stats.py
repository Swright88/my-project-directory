from lib.grammar_stats import *
import pytest

"""Given text to check
check that the type is that of a string"""
def test_text_is_string():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check(25)
    error_message = str(e.value)
    assert error_message == "This is not a valid string"

"""Given a string
check that it begins with a capital letter and ends with punctuation"""
def test_string_upper_and_punc():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello how are you?")
    assert result == True
    
"""Check the percentage of tests checked returns as a integer"""
def test_check_percentages():
    grammar_stats = GrammarStats()
    grammar_stats.check("hello how are you")
    grammar_stats.check("Hello how are you.")
    result = grammar_stats.percentage_good()
    assert result == 50
    
def test_check_percentages_none():
    grammar_stats = GrammarStats()
    result = grammar_stats.percentage_good()
    assert result == 0