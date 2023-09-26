from typing import Union

from fastapi import APIRouter

from app.user import contracts
from app.user.constants import USERS

router = APIRouter(prefix="/users")


@router.get("/")
async def read_user():
    """
    Вывод списка зарегистрированных в системе пользователей.
    :return: список зарегистрированных пользователей
    """
    users_list = []
    for user in USERS:
        users_list.append({
            "username": user.username,
            "name": user.name,
            "surname": user.surname
        })
    return users_list


@router.post("/signup/")
def signup(username: str, password: str,
           email: Union[str, None] = None,
           name: Union[str, None] = None,
           surname: Union[str, None] = None):
    """
    Регистрация нового пользователя.
    В текущей версии введенные данные не сохраняются.
    :param surname: фамилия нового пользователя
    :param name: имя нового пользователя
    :param email: email нового пользователя
    :param password: пароль нового пользователя (обязательно для заполнения)
    :param username: имя в системе нового пользователя (обязательно для заполнения)
    :return: словарь данных нового пользователя
    """
    user_info = contracts.User(
        username=username,
        password=password,
        email=email,
        surname=surname,
        name=name
    )
    return user_info.dict()


@router.post("/login/")
def login(username: str, password: str):
    """
    Вход зарегистрированного в системе пользователя.
    В текущей версии обработка не производится.
    :param username: имя пользователя
    :param password: пароль
    :return: имя в системе и пароль пользователя
    """
    return {"username": username, "password": password}


@router.get("/{username}")
async def read_user(username: str):
    """
    Вывод данных пользователя по имени пользователя в системе.
    :param username: имя пользователя
    :return: данные пользователя
    """
    users_dict = {user.username: {
        "name": user.name,
        "surname": user.surname,
        "email": user.email
    } for user in USERS}

    if username in users_dict:
        return users_dict[username]
    else:
        return "User with this username is not registered"
