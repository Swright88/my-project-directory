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