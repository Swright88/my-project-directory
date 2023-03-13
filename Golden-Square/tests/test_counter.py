from lib.counter import *

def test_counter():
    counter = Counter()
    result = counter.add(5)
    assert counter.report() == "Counted to 5 so far."