from lib.diary import *
from lib.DiaryEntry import *
"""
when multiple entries added
all() lists them in order
"""
def test_adds_to_list(0)
diary = Diary()
    entry1 = DiaryEntry("My Title1", "My Contents1")
    entry2 = DiaryEntry("My Title2", "My Contents2")
    entry3 = DiaryEntry("My Title3", "My Contents3")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    assert diary.all() == [entry1, entry2, entry3]


""" Give an entry with a title and contents """
entry = DiaryEntry("My Title", "My Contents")
entry.title == "My Title"
entry.contents == "My Contents"