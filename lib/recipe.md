# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

Count how many minutes it will take to read the given number of words.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._
def minutes_to_read_text(word_count):
    """ Provides the number of words from a passage of text and counts how many minutes it will take to read the text.

    Parameters: 
        word_count: a parameter of int,  which will be the total number of words in a piece of text
    
    Returns:
        A string which will give the number (int) of minutes it will take to read the text.

```python


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""Given a number of words
It returns the amount of minutes it will take to read. """
minutes_to_read_text(1000) == "It will take 5 minutes to read 1000 words."

"""Given a negative number
It returns an Exception error"""
minutes_to_read_text_neagtive(-200) == Exception "You can not have a negative number of words!"

"""Given a boolean instead of a number of words
It returns an Exception error """
minutes_to_read_text_boolean(True) == Exception "You have not entered a number in the correct format"
"""
Given an empty parameter
It returns an exception error """
minutes_to_read_text_none() == Exception "You have not given a number value"


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

<!-- END GENERATED SECTION DO NOT EDIT -->