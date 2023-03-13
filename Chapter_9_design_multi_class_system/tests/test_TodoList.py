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
TaskList has no incomplete tasks  """
task.list == TaskList()
task_list.all_incomplete() == []

"""
TaskList has no complete tasks  """
task.list == TaskList()
task_list.all_complete() == []
