import math

class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        self.title = title
        self.contents = contents
        pass

    def format(self):
        return f"{self.title}: {self.contents}"
        pass

    def count_words(self):
        words = self.format().split()
        return len(words)
        pass

    def reading_time(self, wpm):
        contents_word_total = len(self.contents.split())
        return math.ceil(contents_word_total / wpm)

    def reading_chunk(self, wpm, minutes):
        words_can_read = wpm * minutes
        word = self.contents.split()
        chunk_of_words = word[:words_can_read]
        return " ".join(chunk_of_words)
        