from lib.mock_diary import *
from unittest.mock import *

def test_word_count_in_all_entries():
    diary = Diary()
    four_word_entry_mock1 = Mock()
    three_word_entry_mock1 = Mock()
    four_word_entry_mock1.count_words.return_value = 4
    three_word_entry_mock1.count_words.return_value = 3
    diary.add(three_word_entry_mock1)
    diary.add(four_word_entry_mock1)
    assert diary.count_words() == 7


