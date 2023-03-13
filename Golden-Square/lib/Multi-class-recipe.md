# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries


## 2. Design the Class System

https://excalidraw.com/#json=yj8wwNahOem_gzPanq4NJ,vEadaDlh7sCaWm15V-EYTQ

```

_Also design the interface of each class in more detail._

```python
class Diary():
    # User-facing properties:
    #   list_of_entries - a list that will hold all the entries inside

    def add(self, diary_entry):
        diary_entry - instance of DiaryEntry
        returns nothing

    def all(self):
        # returns list of DiaryEntry instances

class DiaryEntry():
    # User-facing properties:
    #   title: string representing an entry title
    #   contents: string representing entry contents

    def __init__(self, title, contents):
        #   title: string of entry title
        #   contents: string of entry contents
        # Side-effects:
        #   Sets the above properties

class TaskList():
    def add(self, task)
        # task: an instance of Task
        # returns nothing
        # side-effect: adds to list of tasks

    def all_incompete(self):
        # returns a list of instances of task
        #   represnting the incomplete tasks

    def all_complete(self):
        # returns a list of instances of task
        #   represnting the complete tasks

class Task():
    # Public properties:
    # title: string of job to do

    def __init__(self, title)
        # title: string of job to do
        # side-effect: sets title property

     def mark_complete(self):
        # side-effect: marks task as complete

class PhoneNumberFinder():
    def__init__(self, diary)
        # diary: an instance of Diary
        # side-effect: set diary property

    def find_num(self):
        # returns of list strings containing phone numbers

class Readablechunks():
    def __init__(self, diary)
        # diary: instance of Diary
        # sets diary property

    def extract(self, wpm, mins):
        # wpm: int
        #mins: int
        # returns diary entry that can be read at a 
        # given speed and time 



```         

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

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





## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

#Diary
"""
initially DiaryEntry has no entries """

diary = Diary()
diary.all() == []

#DiaryEntry
""" Give an entry with a title and contents """
entry = DiaryEntry("My Title", "My Contents")
entry.title == "My Title"
entry.contents == "My Contents"

#TaskList
"""
TaskList has no incomplete tasks  """
task.list == TaskList()
task_list.all_incomplete() == []

"""
TaskList has no complete tasks  """
task.list == TaskList()
task_list.all_complete() == []

#Task
"""
Task is given """
task = Task("Go Shopping")




_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

<!-- END GENERATED SECTION DO NOT EDIT -->