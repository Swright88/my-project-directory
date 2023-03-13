"""
when multiple entries added
all() lists them in order
"""
diary = Diary()
entry1 = DiaryEntry("My Title1", "My Contents1")
entry2 = DiaryEntry("My Title2", "My Contents2")
entry3 = DiaryEntry("My Title3", "My Contents3")
diary.add(diary_entry1)
diary.add(diary_entry2)
diary.add(diary_entry3)
diary.all() == [entry1, entry2, entry3]

"""
When multiple tasks added, all_incomplete()
will list them """
task.list = TaskList()
task1 == Task("Go shopping")
task2 = Task("Wash the dishes")
task3 = Task("Go fishing")
task_list.add(task1)
task_list.add(task1)
task_list.add(task1)
task_list.all_incomplete() == [task1, task2, task3]

"""
When multiple tasks added and one marked as complete, all_incomplete()
will list the incomplete tasks """
task.list = TaskList()
task1 == Task("Go shopping")
task2 = Task("Wash the dishes")
task3 = Task("Go fishing")
task_list.add(task1)
task_list.add(task1)
task_list.add(task1)
task3.mark_complete()
task_list.all_incomplete() == [task1, task2]

"""
When multiple tasks added and one left as incomplete, all_complete()
will list the complete tasks """
task.list = TaskList()
task1 == Task("Go shopping")
task2 = Task("Wash the dishes")
task3 = Task("Go fishing")
task_list.add(task1)
task_list.add(task1)
task_list.add(task1)
task3.mark_complete()
task_list.all_complete() == [task3]

"""
When multiple entries added, call phonenumberfinder
and return a list of numbers from entries """
diary = Diary()
entry1 = DiaryEntry("My Title1", "Friends number is 07345678911")
entry2 = DiaryEntry("My Title2", "Friends number is 07123456789")
entry3 = DiaryEntry("My Title3", "My Contents3")
diary.add(diary_entry1)
diary.add(diary_entry2)
diary.add(diary_entry3)
extractor == PhoneNumberFinder(diary)
extractor.find_num() == ["07345678911", "07123456789"]

""" 
When multiple entries added, call phonenumberfinder
and return a list of numbers from entries, do not return non-valid 
numbers """
diary = Diary()
entry1 = DiaryEntry("My Title1", "Friends number is 0734567891123")
entry2 = DiaryEntry("My Title2", "Friends number is 07123456789")
entry3 = DiaryEntry("My Title3", "My Contents3")
diary.add(diary_entry1)
diary.add(diary_entry2)
diary.add(diary_entry3)
extractor == PhoneNumberFinder(diary)
extractor.find_num == ["07123456789"]

"""
When I add a diary entry, get back the one that fits the time 
and  """
diary = Diary()
entry1 = DiaryEntry("Title", "one two three four")
diary.add(entry1)
extractor = ReadableChunks(diary)
extractor.extract(wpm=2, minutes=2) === entry1

"""
When I ad an entry that does not fit wpm and time
return none """
diary = Diary()
entry1 = DiaryEntry("Title", "one two three four five")
diary.add(entry1)
extractor = ReadableChunks(diary)
extractor.extract(wpm=2, minutes=2) === entry1

"""
initially DiaryEntry has no entries """

diary = Diary()
diary.all() == []
