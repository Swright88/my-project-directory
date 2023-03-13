from lib.gratitude import *

def test_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("your health")
    assert gratitude.format() == "Be grateful for: your health"
    