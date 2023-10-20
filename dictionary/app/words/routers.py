from typing import List

from fastapi import APIRouter

from . import contracts

router = APIRouter(prefix="/words")
WORDS_DICT = contracts.WordsDict()


@router.get("/")
async def get_all_words():
    """
    Возвращает список всех слов, сохраненных в словаре,
    отсортированных в алфавитном порядке.

    :return: List[contracts.Word] - список слов в словаре
    """
    return WORDS_DICT.words_dict


@router.post("/{word}")
async def add_word(word: str, translation: str):
    """
    Функция для добавления нового слова в словарь.

    :param word: Новое слово.
    :param translation: Перевод.
    :return: Ответ об успешном добавлении слова.
    """
    if WORDS_DICT.find_word(word) is not None:
        return {"message": f"Слово '{word}' уже есть в словаре"}
    else:
        WORDS_DICT.append_word(word, translation)
        return {"message": f"Слово '{word}' добавлено в словарь"}


@router.delete("/{word}")
async def remove_word(word: str):
    """
    Функция для удаления слова из словаря

    :param word: Слово для удаления
    :return: Ответ об успешном удалении слова
    """
    word_id = WORDS_DICT.find_word(word)
    if word_id is not None:
        WORDS_DICT.remove_word(word_id)
        return {"message": f"Слово '{word}' удалено из словаря"}
    else:
        return {"message": f"Слова '{word}' нет в словаре"}


@router.get("/{word}")
async def find_word(word: str):
    """
    Функция для поиска слова в словаре

    :param word: Слово для поиска.
    :return: Слово и его перевод, либо ответ об отсутствии слова в словаре
    """
    word_id = WORDS_DICT.find_word(word)
    if word_id is not None:
        return WORDS_DICT.words_dict[word_id].model_dump()
    else:
        return {"message": f"Слова '{word}' нет в словаре"}
