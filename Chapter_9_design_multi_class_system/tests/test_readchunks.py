"""
When I add a diary entry, get back the one that fits the time 
and  """
diary = Diary()
entry1 = DiaryEntry("Title", "one two three four")
diary.add(entry1)
extractor = ReadableChunks(diary)
extractor.extract(wpm=2, minutes=2) === entry1

"""
When I add an entry that does not fit wpm and time
return none """
diary = Diary()
entry1 = DiaryEntry("Title", "one two three four five")
diary.add(entry1)
extractor = ReadableChunks(diary)
extractor.extract(wpm=2, minutes=2) === entry1