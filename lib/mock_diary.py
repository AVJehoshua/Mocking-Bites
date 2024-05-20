# File: lib/diary.py

class Diary:
    # Public properties:
    #   entries: a list of instances of DiaryEntry

    def __init__(self):
        self.list_entry = []

    def add(self, entry):
        # entry is an instance of DiaryEntry
        self.list_entry.append(entry)

    def count_words(self):
        # Returns the number of words in all entries
        return sum([entry.count_words() for entry in self.list_entry])
        