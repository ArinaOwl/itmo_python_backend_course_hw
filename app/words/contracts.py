from pydantic import BaseModel
from typing import List


class Word(BaseModel):
    """
    Данные слова в словаре: слово и перевод
    """
    word: str
    translation: str


class WordsDict(object):
    """
    Словарь
    """
    def __init__(self, words: List[Word] = None):
        if words is None:
            self.words_dict = []
        else:
            self.words_dict = words

    def __len__(self):
        return len(self.words_dict)

    def find_word(self, word: str):
        """
        Поиск слова в словаре.

        :param word: Слово для поиска.
        :return: индекс слова в словаре
        """
        word_id = 0
        for note in self.words_dict:
            if note.word == word:
                return word_id
            word_id += 1
        return None

    def sort_words(self):
        """
        Сортировка словаря в алфавитном порядке по сохраненным словам
        """
        self.words_dict = sorted(self.words_dict, key=lambda d: d.word)

    def append_word(self, word, translation):
        """
        Добавление нового слова в словарь с сортировкой словаря после добавления.

        :param word: Новое слово.
        :param translation: Перевод.
        """
        self.words_dict.append(Word(word=word, translation=translation))
        self.sort_words()

    def remove_word(self, word_id):
        """
        Удаление слова из словаря по индексу

        :param word_id: индекс удаляемого слова
        """
        del self.words_dict[word_id]
