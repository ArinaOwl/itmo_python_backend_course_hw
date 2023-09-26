from typing import Union
from pydantic import BaseModel


class User(BaseModel):
    """
    Данные пользователя
    """
    username: str
    password: str
    email: Union[str, None] = None
    name: Union[str, None] = None
    surname: Union[str, None] = None
