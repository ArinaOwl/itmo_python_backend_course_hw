from typing import Union
from pydantic import BaseModel, field_validator, model_validator


class UserLogin(BaseModel):
    """
    Данные пользователя для входа
    """
    username: str
    password: str


class UserSignup(BaseModel):
    """
    Данные пользователя для регистрации
    """
    username: str
    password: str
    email: Union[str, None] = None
    name: Union[str, None] = None
    surname: Union[str, None] = None


class UserUpdateDictRequest(BaseModel):
    """
    Данные для изменения словаря
    """
    word: str
    action_type: str
    translation: Union[str, None] = None

    @field_validator('action_type')
    @classmethod
    def available_action_type(cls, v: str) -> str:
        """
        Проверка что действие со словарем доступно

        param v: значение поля 'action_type'
        return: значение поля 'action_type', приведенное к нижнему регистру
        """
        available_action_types = ["add", "remove"]
        if v.lower() not in available_action_types:
            raise ValueError('must be "add" or "remove"')
        return v.lower()

    @model_validator(mode='after')
    def check_translation(self) -> 'UserModel':
        """
        Проверка на наличие перевода при добавлении нового слова
        return:
        """
        if self.action_type == 'add' and self.translation is None:
            raise ValueError('to add word need a translation')
        return self




