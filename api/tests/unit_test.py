import pytest

from app.contracts import UserUpdateDictRequest


@pytest.mark.parametrize(
    "word, action_type, translation, saved_action_type",
    [
        ('test', 'add', 'test', 'add'),
        ('test', 'remove', None, 'remove'),
        ('test', 'Remove', None, 'remove'),
    ]
)
def test_available_action_type_valid(word, action_type, translation, saved_action_type):
    """
    Тест на правильность валидации action_type при использовании доступных значений.
    Ожидается, что метод available_action_type вернет значение action_type в нижнем регистре.
    """
    user_request = UserUpdateDictRequest(word=word, action_type=action_type, translation=translation)
    assert user_request.action_type == saved_action_type


def test_available_action_type_invalid():
    """
    Тест на валидацию action_type при использовании недопустимого значения.
    Ожидается, что будет возбуждено исключение ValueError.
    """
    with pytest.raises(ValueError):
        UserUpdateDictRequest(word='test', action_type='invalid')


def test_check_translation_missing():
    """
    Тест на проверку наличия перевода при добавлении нового слова.
    Ожидается, что будет возбуждено исключение ValueError.
    """
    with pytest.raises(ValueError):
        UserUpdateDictRequest(word='test', action_type='add', translation=None)


def test_check_translation_not_required():
    """
    Тест на проверку наличия перевода при удалении слова.
    Ожидается, что метод check_translation не вызовет исключение.
    """
    user_request = UserUpdateDictRequest(word='test', action_type='remove', translation=None)
    user_request.action_type = 'remove'
