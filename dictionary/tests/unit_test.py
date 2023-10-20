import pytest

from app.words.contracts import Word, WordsDict


@pytest.fixture
def words_dict():
    """
    Фикстура для инициализации объекта класса Словарь, заполненного фиксированными значениями
    """
    return WordsDict([
        Word(word='banana', translation='банан'),
        Word(word='apple', translation='яблоко'),
        Word(word='cherry', translation='вишня'),
        Word(word='watermelon', translation='арбуз'),
        Word(word='tomato', translation='помидор'),
        Word(word='grape', translation='виноград')
    ])


@pytest.mark.parametrize(
    "word, word_id",
    [
        ('apple', 1),
        ('cherry', 2),
        ('grape', 5),
        ('cucumber', None)
    ]
)
def test_find_word_in_dict(words_dict, word, word_id):
    """ Тест поиска слова в словаре """
    result = words_dict.find_word(word)
    assert result == word_id


@pytest.mark.parametrize(
    "word, translation, word_id",
    [
        ('apple', 'яблоко', 0),
        ('grape', 'виноград', 3),
        ('watermelon', 'арбуз', 5),
    ]
)
def test_sort_words_in_dict(words_dict, word, translation, word_id):
    """ Тест сортировки слов в словаре по алфавиту """
    words_dict.sort_words()
    result = words_dict.words_dict[word_id]
    assert result.word == word
    assert result.translation == translation


@pytest.mark.parametrize(
    "word, word_id",
    [
        ('apple', 1),
        ('tomato', 4),
        ('watermelon', 3),
    ]
)
def test_remove_words_in_dict(words_dict, word, word_id):
    """ Тест удаления слова из словаря """
    words_dict.remove_word(word_id)
    result = words_dict.words_dict[word_id]
    assert result.word != word
    assert len(words_dict) == 5
