from lib.diary_entry import *
#Define entries to the class 
#Ensuring they are in the correct format

"""Given a title and content
return them in the correct format"""

def test_format_and_content():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"
    
    """Given the title and contents
    return the total number of words"""
    
def test_count_words():
    diary_entry = DiaryEntry("My title", "contents")
    result = diary_entry.count_words() 
    assert result == 3
        
    """Given the contents
    return the an estimated time it will take to read with a wpm of 2"""
def test_reading_time_using_wpm_of_2():
    diary_entry = DiaryEntry("My title", "hello there I hope you are well today")
    result = diary_entry.reading_time(2)
    assert result == 4        
        
def test_reading_time_using_wpm_odd_num():
    diary_entry = DiaryEntry("My title", "hello there I hope you are well ")
    result = diary_entry.reading_time(2)
    assert result == 4     
    
    """Given a contents 6 words long
    Given a wpm of 2 and 2 minutes
    Return the first 4 words of the contents"""
def test_reading_chunk_given():
    diary_entry = DiaryEntry("My title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "one two three four"