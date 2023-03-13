# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

Check and confirm the sentance starts with a capital letter and ends with either a fullstop, exclamation mark or question mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._
def grammar_check(string):
    """ Takes a given string and checks for a capital letter at the start and a suitable puncutaion to end with.

    Parameters: 
        string: a string sentence to be checked. 
    
    Returns:
        True if the conditions are met otherwise False

```python


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""Given a number of suitable string
It checks the conditions and returns True"""
grammar_check_true(Hello how are you today?)== True

"""Given a number of suitable string
It checks the conditions and returns False"""
grammar_check_false(hi nice to meet you)== False


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE



```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

<!-- END GENERATED SECTION DO NOT EDIT -->