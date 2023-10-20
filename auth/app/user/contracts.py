from typing import Union
from pydantic import BaseModel


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
