import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    """ Тест получения данных в корневом разделе """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World"


@pytest.mark.parametrize(
    "username, password, email, name, surname",
    [
        ('arina_owl', '88888888', 'arina.u@example.ru', 'Arina', 'Ushch'),
        ('lyosha19', '1234', None, None, None),
    ]
)
def test_signup(username, password, email, name, surname):
    """ Тест на успешную регистрацию нового пользователя"""
    request_json = {
        "username": username,
        "password": password,
        "email": email,
        "name": name,
        "surname": surname
    }
    response = client.post(f"/signup", json=request_json)
    assert response.status_code == 200
    assert response.json() == request_json


@pytest.mark.parametrize(
    "username, password",
    [
        ('arina_owl', '88888888'),
        ('lyosha19', '1234'),
    ]
)
def test_signup(username, password):
    """ Тест на успешную регистрацию нового пользователя"""
    request_json = {
        "username": username,
        "password": password
    }
    response = client.post(f"/login", json=request_json)
    assert response.status_code == 200
    assert response.json() == request_json


@pytest.mark.parametrize(
    "word, action_type, translation, response_json",
    [
        ('apple', 'add', 'яблоко', {'message': "Слово 'apple' добавлено в словарь"}),
        ('apple', 'add', 'яблоко', {'message': "Слово 'apple' уже есть в словаре"}),
        ('grape', 'add', 'виноград', {'message': "Слово 'grape' добавлено в словарь"}),
        ('apple', 'remove', None, {'message': "Слово 'apple' удалено из словаря"}),
        ('apple', 'remove', None, {'message': "Слова 'apple' нет в словаре"}),
        ('grape', 'remove', None, {'message': "Слово 'grape' удалено из словаря"}),
        ('apple', 'add', 'яблоко', {'message': "Слово 'apple' добавлено в словарь"}),
        ('grape', 'add', 'виноград', {'message': "Слово 'grape' добавлено в словарь"}),
    ]
)
def test_update_dict(word, action_type, translation, response_json):
    """ Тест редактирования словаря"""
    request_json = {
        "word": word,
        "action_type": action_type,
        "translation": translation
    }
    response = client.post(f"/update_dictionary", json=request_json)
    assert response.status_code == 200
    assert response.json() == response_json


@pytest.mark.parametrize(
    "word, response_json",
    [
        ('apple', {'translation': 'яблоко', 'word': 'apple'}),
        ('grape', {'translation': 'виноград', 'word': 'grape'}),
        ('tomato', {'message': "Слова 'tomato' нет в словаре"})
    ]
)
def test_read_dict(word, response_json):
    """ Тест поиска слова в словаре"""
    response = client.get(f"/read_dictionary/{word}")
    assert response.status_code == 200
    assert response.json() == response_json
