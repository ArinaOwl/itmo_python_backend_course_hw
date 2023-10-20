import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    """ Тест получения данных в корневом разделе """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Редактируемая тетрадь для записи иностранных слов"}


@pytest.mark.parametrize(
    "word, translation, status_code, json_msg",
    [
        ('apple', 'яблоко', 200, {"message": f"Слово 'apple' добавлено в словарь"}),
        ('tomato', 'помидор', 200, {"message": f"Слово 'tomato' добавлено в словарь"}),
        ('apple', 'яблоко', 200, {"message": f"Слово 'apple' уже есть в словаре"}),
        ('grape', 'виноград', 200, {"message": f"Слово 'grape' добавлено в словарь"}),
    ]
)
def test_add_word(word, translation, status_code, json_msg):
    """ Тест добавления слова в словарь """
    response = client.post(f"/words/{word}?translation={translation}")
    assert response.status_code == status_code
    assert response.json() == json_msg


@pytest.mark.parametrize(
    "word, status_code, json_msg",
    [
        ('apple', 200, {"message": f"Слово 'apple' удалено из словаря"}),
        ('cucumber', 200, {"message": f"Слова 'cucumber' нет в словаре"})
    ]
)
def test_remove_word(word, status_code, json_msg):
    """ Тест удаления слова из словаря """
    response = client.delete(f"/words/{word}")
    assert response.status_code == status_code
    assert response.json() == json_msg


@pytest.mark.parametrize(
    "word, status_code, json_msg",
    [
        ('tomato', 200, {"word": "tomato", "translation": "помидор"}),
        ('grape', 200, {"word": "grape", "translation": "виноград"}),
        ('cucumber', 200, {"message": f"Слова 'cucumber' нет в словаре"})
    ]
)
def test_find_word(word, status_code, json_msg):
    """ Тест поиска слова в словаре """
    response = client.get(f"/words/{word}")
    assert response.status_code == status_code
    assert response.json() == json_msg


def test_get_all_words():
    """ Тест вывода всех слов в словаре """
    response = client.get("/words/")
    assert response.status_code == 200
    assert response.json() == [
        {"word": "grape", "translation": "виноград"},
        {"word": "tomato", "translation": "помидор"}
    ]
